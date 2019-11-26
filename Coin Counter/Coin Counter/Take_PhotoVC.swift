//
//  Take_PhotoVC.swift
//  Coin Counter
//
//  Created by Jaclyn Stickrod on 10/28/19.
//  Copyright © 2019 Jaclyn Stickrod. All rights reserved.
//

import Foundation

import UIKit

class Take_PhotoVC: UIViewController, UINavigationControllerDelegate, UIImagePickerControllerDelegate {

    @IBOutlet weak var myImageView: UIImageView!
    
    
    @IBAction func import_image(_ sender: Any) {
        let image = UIImagePickerController()
        image.delegate = self
        
        image.sourceType = UIImagePickerController.SourceType.photoLibrary
        
        image.allowsEditing = false
        
        self.present(image, animated: true)
        {
            //AFTER IT IS COMPLETE
        }
        
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any])
    {
        if let image = info[UIImagePickerController.InfoKey.originalImage] as? UIImage
        {
            //setting the myImageView variable to verified image
            //somehow need to take image from here and give it to backend
            myImageView.image = image
        }
        else {
            //Error Message
        }
            
        self.dismiss(animated: true, completion: nil)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    
    
}
