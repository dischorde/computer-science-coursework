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
    private var operationSequence: String?
    
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
                accumulator = value
                operationSequence = symbol
            case .unaryOperation(let function):
                if accumulator != nil {
                    operationSequence = symbol + "(\(accumulator!))"
                    accumulator = function(accumulator!)
                }
            case .binaryOperation(let function):
                if accumulator != nil {
                    pendingBinaryOperation = PendingBinaryOperation(function: function, firstOperand: accumulator!)
                    operationSequence = "\(accumulator!) " + symbol
                    accumulator = nil
                }
            case .equals:
                if operationSequence != nil {
                    operationSequence = operationSequence! + " \(accumulator!)"
                }
                performPendingBinaryOperation()
            case .clear:
                pendingBinaryOperation = nil
                accumulator = 0
            }
        }
        print(operationSequence)
    }
    
    private mutating func performPendingBinaryOperation() {
        if pendingBinaryOperation != nil && accumulator != nil {
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
    
    mutating func setOperand(_ operand: Double) {
        accumulator = operand
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
}

