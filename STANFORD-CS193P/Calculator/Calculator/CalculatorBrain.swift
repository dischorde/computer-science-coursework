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
    private var sequenceOfOperations = ""
    
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
                sequenceOfOperations = sequenceOfOperations + " " + symbol
            case .unaryOperation(let function):
                if accumulator != nil {
                    if resultIsPending {
                        sequenceOfOperations = sequenceOfOperations + " " + symbol + "(\(accumulator!))"
                    } else {
                        sequenceOfOperations = symbol + "(\(sequenceOfOperations))"
                    }
                    accumulator = function(accumulator!)
                }
            case .binaryOperation(let function):
                if pendingBinaryOperation != nil {
                    performPendingBinaryOperation()
                }
                if accumulator != nil {
                    pendingBinaryOperation = PendingBinaryOperation(function: function, firstOperand: accumulator!)
                    sequenceOfOperations = sequenceOfOperations + " " + symbol
                    accumulator = nil
                }
            case .equals:
                performPendingBinaryOperation()
            case .clear:
                pendingBinaryOperation = nil
                accumulator = 0
                sequenceOfOperations = ""
            }
        }
        print(sequenceOfOperations)
    }
    
    private mutating func performPendingBinaryOperation() {
        if resultIsPending && accumulator != nil {
            sequenceOfOperations = sequenceOfOperations + " \(accumulator!)"
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
        if sequenceOfOperations == "" || !resultIsPending {
            sequenceOfOperations = String(operand)
        }
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

