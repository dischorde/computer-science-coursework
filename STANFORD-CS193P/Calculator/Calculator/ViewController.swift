//
//  ViewController.swift
//  Calculator
//
//  Created by Katarina Rossi on 9/18/17.
//  Copyright © 2017 Katarina Rossi. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    
    @IBOutlet weak var display: UILabel?
    
    var userIsInTheMiddleOfTyping = false
    
    @IBAction func touchDigit(_ sender: UIButton) {
        let digit = sender.currentTitle!
        if userIsInTheMiddleOfTyping {
            let textCurrentlyInDisplay = display!.text!
            display!.text = textCurrentlyInDisplay + digit
        } else {
            display!.text = digit
            userIsInTheMiddleOfTyping = true
        }
        
    }
    
    
    @IBAction func performOperation(_ sender: UIButton) {
        if let mathematicalOperation = sender.currentTitle {
            switch mathematicalOperation {
            case "π":
                display!.text = "3.1415926"
            default:
                break
            }
        }
    }
    
}

