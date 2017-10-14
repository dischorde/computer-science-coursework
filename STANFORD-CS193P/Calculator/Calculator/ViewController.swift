//
//  ViewController.swift
//  Calculator
//
//  Created by Katarina Rossi on 9/18/17.
//  Copyright © 2017 Katarina Rossi. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    
    @IBOutlet weak var descriptionLabel: UILabel!
    @IBOutlet weak var display: UILabel!
    
    var userIsInTheMiddleOfTyping = false
    
    @IBAction func touchDigit(_ sender: UIButton) {
        let digit = sender.currentTitle!
        if userIsInTheMiddleOfTyping {
            let textCurrentlyInDisplay = display.text!
            display.text = textCurrentlyInDisplay + digit
        } else {
            display.text = digit
            userIsInTheMiddleOfTyping = true
        }
        updateDescriptionLabel()
        
    }
    
    @IBAction func touchDecimal(_ sender: UIButton) {
        if userIsInTheMiddleOfTyping {
            let textCurrentlyInDisplay = display.text!
            let potentialNewDisplayText = textCurrentlyInDisplay + "."
            if Double(potentialNewDisplayText) != nil {
                display.text = potentialNewDisplayText
            }
        } else {
            display.text = "0."
            userIsInTheMiddleOfTyping = true
        }
        updateDescriptionLabel()
    }
    
    @IBAction func backspace(_ sender: UIButton) {
        if userIsInTheMiddleOfTyping {
            var textToBeDisplayed = display.text!
            textToBeDisplayed.characters.removeLast()
            if textToBeDisplayed == "" {
                textToBeDisplayed = "0"
                userIsInTheMiddleOfTyping = false
            }
            display.text = textToBeDisplayed
        }
        updateDescriptionLabel()
    }
    
    var displayValue: Double {
        get {
            return Double(display.text!)!
        }
        set {
            display.text = String(format: "%g", newValue)
        }
    }
    
    private var brain: CalculatorBrain = CalculatorBrain()
    
    
    @IBAction func performOperation(_ sender: UIButton) {
        if userIsInTheMiddleOfTyping {
            brain.setOperand(displayValue)
            userIsInTheMiddleOfTyping = false
        }
        if let mathematicalSymbol = sender.currentTitle {
            brain.performOperation(mathematicalSymbol)
        }
        if let result = brain.result {
            displayValue = result
        }
        updateDescriptionLabel()
    }
    
    func updateDescriptionLabel() {
        if brain.resultIsPending {
            descriptionLabel.text = brain.description + "..."
        } else if brain.description != "" {
            descriptionLabel.text = brain.description + " = "
        } else {
            descriptionLabel.text = ""
        }
    }
}
