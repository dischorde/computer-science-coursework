//
//  Concentration.swift
//  Concentration
//
//  Created by Katarina Rossi on 5/18/18.
//  Copyright © 2018 Katarina Rossi. All rights reserved.
//

import Foundation
import GameplayKit.GKRandomSource

class Concentration
{
    var cards = [Card]()
    var flipCount = 0
    var score = 0
    var previouslySeenIndexes = Set<Int>()
    
    var indexOfOneAndOnlyFaceUpCard: Int?
    
    init(numberOfPairsOfCards: Int) {
        for _ in 1...numberOfPairsOfCards {
            let card = Card()
            cards += [card, card]
        }
        cards = GKRandomSource.sharedRandom().arrayByShufflingObjects(in: cards) as! [Card]
    }
    
    func chooseCard(at index: Int) {
        guard !cards[index].isMatched else { return } // return if card is already matched

        flipCount += 1

        if let matchIndex = indexOfOneAndOnlyFaceUpCard, matchIndex != index {
            if cards[matchIndex].doesMatch(cards[index]) {
                cards[matchIndex].isMatched = true
                cards[index].isMatched = true
                score += 2
            } else if previouslySeenIndexes.contains(index) && previouslySeenIndexes.contains(matchIndex) {
                score -= 2
            } else if previouslySeenIndexes.contains(index) || previouslySeenIndexes.contains(matchIndex) {
                score -= 1
            }
            cards[index].isFaceUp = true
            indexOfOneAndOnlyFaceUpCard = nil
            previouslySeenIndexes.insert(index)
            previouslySeenIndexes.insert(matchIndex)
        } else {
            flipEverythingFaceDown()
            cards[index].isFaceUp = true
            indexOfOneAndOnlyFaceUpCard = index
        }
    }
    
    func flipEverythingFaceDown() {
        for flipDownIndex in cards.indices {
            cards[flipDownIndex].isFaceUp = false
        }
    }
}
