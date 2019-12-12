import UIKit
import Foundation
//import CoreML
//import Vision
 
class take_photo:UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate{
    
    @IBOutlet var myImageView: UIImageView!
    
    let imagePicker = UIImagePickerController()
    
    @IBAction func Take_Photo(_ sender: UIButton) {
        imagePicker.allowsEditing = false
        imagePicker.sourceType = .photoLibrary
        present(imagePicker, animated: true, completion: nil)
    }
    var answerString = "Price Amount"
    
    @IBOutlet weak var veiwPrice: UILabel!
    
    @IBAction func Capture(_ sender: Any) {
//        imagePicker.sourceType = .camera
//        present(imagePicker, animated: true, completion: nil)
       
    }
    
    override func viewDidLoad() {
       super.viewDidLoad()
        imagePicker.delegate = self
//        imagePicker.allowsEditing = true
    }
    
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        
        if let pickedImage = info[UIImagePickerController.InfoKey.originalImage] as? UIImage {
            myImageView.contentMode = .scaleAspectFit
            myImageView.image = pickedImage
            connectHeroku(image: pickedImage)
        }
        
        dismiss(animated: true, completion: nil)
    }
    
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        dismiss(animated: true, completion: nil)
    }
    
    
    func connectHeroku(image: UIImage ){
            var r  = URLRequest(url: URL(string: "https://flask-3308.herokuapp.com/count_coins")!)
            r.httpMethod = "POST"
            let boundary = "Boundary-\(UUID().uuidString)"
            r.setValue("multipart/form-data; boundary=\(boundary)", forHTTPHeaderField: "Content-Type")
            
            
            r.httpBody = createBody(boundary: boundary,
                                    data: image.jpegData(compressionQuality:0.1)!,
                                    mimeType: "image/jpg",
                                    filename: "file.jpg")
            
            print("it sends!")
  
            let task = URLSession.shared.dataTask(with: r) { data, response, error in
                guard let data = data,
                    let response = response as? HTTPURLResponse,
                    error == nil else {                                              // check for fundamental networking error
                    print("error", error ?? "Unknown error")
                    return
                }

                guard (200 ... 299) ~= response.statusCode else {                    // check for http errors
                    print("statusCode should be 2xx, but is \(response.statusCode)")
                    print("response = \(response)")
                    return
                }
                let responseString = String(data: data, encoding: .utf8)!
                self.answerString = String(describing: responseString)
                print("responseString = \(String(describing: responseString))")
                DispatchQueue.main.async {
                    self.veiwPrice.text = self.answerString
                }
                
              }
            task.resume()
            
        }
   
    func createBody(boundary: String,
                    data: Data,
                    mimeType: String,
                    filename: String) -> Data {
        let body = NSMutableData()
        body.append("--\(boundary)\r\n".data(using: String.Encoding.utf8)!)
        body.append("Content-Disposition:form-data; name=\"image\"\r\n\r\n".data(using: String.Encoding.utf8)!)
        body.append("hi\r\n".data(using: String.Encoding.utf8)!)
        body.append("--\(boundary)\r\n".data(using: String.Encoding.utf8)!)
        body.append("Content-Disposition:form-data; name=\"file\"; filename=\"\(filename)\"\r\n".data(using: String.Encoding.utf8)!)
        body.append("Content-Type: \(mimeType)\r\n\r\n".data(using: String.Encoding.utf8)!)
        body.append(data)
        body.append("\r\n".data(using: String.Encoding.utf8)!)
        body.append("--\(boundary)--\r\n".data(using: String.Encoding.utf8)!)
        
        return body as Data
    }
    
}

extension Dictionary {
    func percentEscaped() -> String {
        return map { (key, value) in
            let escapedKey = "\(key)".addingPercentEncoding(withAllowedCharacters: .urlQueryValueAllowed) ?? ""
            let escapedValue = "\(value)".addingPercentEncoding(withAllowedCharacters: .urlQueryValueAllowed) ?? ""
            return escapedKey + "=" + escapedValue
        }
        .joined(separator: "&")
    }
}

extension CharacterSet {
    static let urlQueryValueAllowed: CharacterSet = {
        let generalDelimitersToEncode = ":#[]@" // does not include "?" or "/" due to RFC 3986 - Section 3.4
        let subDelimitersToEncode = "!$&'()*+,;="

        var allowed = CharacterSet.urlQueryAllowed
        allowed.remove(charactersIn: "\(generalDelimitersToEncode)\(subDelimitersToEncode)")
        return allowed
    }()
}



