//
//  Card.swift
//  Concentration
//
//  Created by Katarina Rossi on 5/18/18.
//  Copyright © 2018 Katarina Rossi. All rights reserved.
//

import Foundation

struct Card
{
    var isFaceUp = false
    var isMatched = false
    var identifier: Int

    static var identifierFactory = 0
    
    static func getUniqueIdentifier() -> Int {
        identifierFactory += 1
        return identifierFactory
    }
    
    init() {
        self.identifier = Card.getUniqueIdentifier()
    }
    
    func doesMatch(_ otherCard: Card) -> Bool {
        return identifier == otherCard.identifier
    }
}
