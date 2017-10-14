//
//  CalculatorBrain.swift
//  Calculator
//
//  Created by Katarina Rossi on 9/18/17.
//  Copyright © 2017 Katarina Rossi. All rights reserved.
//

import Foundation

struct CalculatorBrain {
    
    private var accumulator: Double?
    private var label = displayLabel()
    
    private enum Operation {
        case constant(Double)
        case unaryOperation((Double) -> Double)
        case binaryOperation((Double, Double) -> Double)
        case equals
        case clear
    }
    
    private var operations: Dictionary<String,Operation> = [
        "π" : Operation.constant(Double.pi),
        "e" : Operation.constant(M_E),
        "√" : Operation.unaryOperation(sqrt),
        "sin" : Operation.unaryOperation(sin),
        "cos" : Operation.unaryOperation(cos),
        "tan" : Operation.unaryOperation(tan),
        "x" : Operation.binaryOperation({ $0 * $1 }),
        "+" : Operation.binaryOperation({ $0 + $1 }),
        "-" : Operation.binaryOperation({ $0 - $1 }),
        "÷" : Operation.binaryOperation({ $0 / $1 }),
        "%" : Operation.binaryOperation({ $0.truncatingRemainder(dividingBy: $1) }),
        "=" : Operation.equals,
        "clr" : Operation.clear
    ]
    
    mutating func performOperation(_ symbol: String) {
        if let operation = operations[symbol] {
            switch(operation) {
            case .constant(let value):
                if !resultIsPending {
                    label.clear()
                }
                accumulator = value
                label.updateNextOperand(with: symbol)
            case .unaryOperation(let function):
                if accumulator != nil {
                    if resultIsPending {
                        let nextOperand = symbol + "(\(label.nextOperandToDisplay))"
                        label.updateNextOperand(with: nextOperand)
                        label.computeFullSequence()
                    } else {
                        label.addUnaryOperation(symbol)
                    }
                    accumulator = function(accumulator!)
                }
            case .binaryOperation(let function):
                if pendingBinaryOperation != nil {
                    label.computeFullSequence()
                    performPendingBinaryOperation()
                }
                if accumulator != nil {
                    pendingBinaryOperation = PendingBinaryOperation(function: function, firstOperand: accumulator!)
                    label.addBinaryOperation(symbol)
                    accumulator = nil
                }
            case .equals:
                label.computeFullSequence()
                performPendingBinaryOperation()
            case .clear:
                pendingBinaryOperation = nil
                accumulator = 0
                label.clear()
            }
        }
    }
    
    private mutating func performPendingBinaryOperation() {
        if resultIsPending && accumulator != nil {
            accumulator = pendingBinaryOperation!.perform(with: accumulator!)
            pendingBinaryOperation = nil
        }
    }

    private var pendingBinaryOperation: PendingBinaryOperation?
    
    private struct PendingBinaryOperation {
        let function: (Double, Double) -> Double
        let firstOperand: Double
        
        func perform(with secondOperand: Double) -> Double {
            return function(firstOperand, secondOperand)
        }
    }
    
    private struct displayLabel {
        var sequenceOfOperations = ""
        var nextOperandToDisplay = ""
        
        mutating func addBinaryOperation(_ symbol: String) {
            computeFullSequence()
            sequenceOfOperations = sequenceOfOperations + " " + symbol
        }
        
        mutating func addUnaryOperation(_ symbol: String) {
            computeFullSequence()
            sequenceOfOperations = symbol + "(\(sequenceOfOperations))"
        }
        
        mutating func updateNextOperand(with operand: String) {
            nextOperandToDisplay = operand
        }
        
        mutating func computeFullSequence() {
            if sequenceOfOperations == "" && nextOperandToDisplay != "" {
                sequenceOfOperations = nextOperandToDisplay
            } else if nextOperandToDisplay != "" {
                sequenceOfOperations = sequenceOfOperations + " " + nextOperandToDisplay
            }
            nextOperandToDisplay = ""
        }
        
        mutating func clear() {
            sequenceOfOperations = ""
            nextOperandToDisplay = ""
        }
    }
    
    mutating func setOperand(_ operand: Double) {
        accumulator = operand
        if !resultIsPending {
            label.clear()
        }
        label.updateNextOperand(with: String(format: "%g", operand))
    }
    
    var result: Double? {
        get {
            return accumulator
        }
    }
    
    var resultIsPending: Bool {
        get {
            return pendingBinaryOperation != nil
        }
    }
    
    var description: String {
        get {
            return label.sequenceOfOperations
        }
    }
}

