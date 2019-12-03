//
//  take_photo.swift
//  CoinCounter
//
//  Created by Beka Admasu on 11/15/19.
//  Copyright © 2019 Beka Admasu. All rights reserved.
//

import UIKit

class take_photo: UIViewController {

override func viewDidLoad() {
    super.viewDidLoad()
    // Do any additional setup after loading the view.
}
    @IBOutlet weak var myImageView: UIImageView!

    var imagePicker: UIImagePickerController!
    @IBAction func Take_Photo(_ sender: Any) {
        
            let alert = UIAlertController(title: "First message", message: "Help us train our program by answering a few questions", preferredStyle: UIAlertController.Style.alert)

            alert.addAction(UIAlertAction(title: "Sure!", style: .default, handler: {(action: UIAlertAction!) in
                //call next alert
                alert.dismiss(animated: true, completion: nil)
                //self.quarters_Alert(title: "Next Alert", message: "Go to Quarters")

            }))

            alert.addAction(UIAlertAction(title: "No thanks", style: .default, handler: { (action) in alert.dismiss(animated: true, completion: nil) }))
            
            
            
            
            ///////////////////////////////////
            
            let image = UIImagePickerController()
        image.delegate = self as? UIImagePickerControllerDelegate & UINavigationControllerDelegate
            
            let actionSheet = UIAlertController(title: "Photo Source", message: "Choose a source", preferredStyle: .actionSheet)
            actionSheet.addAction(UIAlertAction(title: "Camera", style: .default, handler: {(action: UIAlertAction) in
                
                if UIImagePickerController.isSourceTypeAvailable(.camera) {
                    image.sourceType = UIImagePickerController.SourceType.camera
                    self.present(image, animated: true, completion: nil)
                }
                else{
                    print("Camera not available")
                }
                
            }))
            actionSheet.addAction(UIAlertAction(title: "Photo Library", style: .default, handler: {(action: UIAlertAction) in
                
                if UIImagePickerController.isSourceTypeAvailable(.photoLibrary){
                    image.sourceType = UIImagePickerController.SourceType.photoLibrary
                    self.present(image, animated: true, completion: nil)
                    //image.dismiss(animated: true, completion: nil)
                }
                else {
                    print("Photo Library is unavailable")
                }
            
                
            }))
            actionSheet.addAction(UIAlertAction(title: "Cancel", style: .cancel, handler: nil))
            
            self.present(actionSheet, animated: true, completion: nil)
            
            
            
        }
        
        override func viewDidAppear(_ animated: Bool) {
            
        }
        
   
        
        
        //info dictionary contains our image data
//        func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any])
//        {
//            let image = info[UIImagePickerController.InfoKey.originalImage] as! UIImage
//            
//            //this actually presents the image on the screen
//            myImageView.image = image
//            
//            picker.dismiss(animated: true, completion: nil)
//        }
//        
//        func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
//            picker.dismiss(animated: true, completion: nil)
//        }
    









}
