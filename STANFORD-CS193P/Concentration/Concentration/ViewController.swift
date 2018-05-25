//
//  ViewController.swift
//  Concentration
//
//  Created by Katarina Rossi on 5/18/18.
//  Copyright © 2018 Katarina Rossi. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    lazy var game =  Concentration(numberOfPairsOfCards: cardButtons.count / 2)

    lazy var currentTheme = chooseRandomTheme()
    
    lazy var emojiChoices = currentTheme.emojis
    
    var emoji = [Int:String]()
    
    @IBOutlet weak var flipCountLabel: UILabel!
    
    @IBOutlet weak var scoreLabel: UILabel!
    
    @IBOutlet var cardButtons: [UIButton]!
    
    @IBAction func touchCard(_ sender: UIButton) {
        if let cardNumber = cardButtons.index(of: sender) {
            game.chooseCard(at: cardNumber)
            updateViewFromModel()
        }
    }
    
    @IBAction func resetGame(_ sender: UIButton) {
        game = Concentration(numberOfPairsOfCards: cardButtons.count / 2)
        resetTheme()
        updateViewFromModel()
    }
    
    func updateViewFromModel() {
        flipCountLabel.text = "Flips: \(game.flipCount)"
        scoreLabel.text = "Score: \(game.score)"
        for index in cardButtons.indices {
            let button = cardButtons[index]
            let card = game.cards[index]
            if card.isFaceUp {
                button.setTitle(emoji(for: card), for: .normal)
                button.backgroundColor = #colorLiteral(red: 1, green: 1, blue: 1, alpha: 1)
            } else {
                
                button.setTitle("", for: .normal)
                button.backgroundColor = backgroundColor(for: card, at: index)
            }
        }
    }
    
    func emoji(for card: Card) -> String {
        if emoji[card.identifier] == nil, emojiChoices.count > 0 {
            let randomIndex = Int(arc4random_uniform(UInt32(emojiChoices.count)))
            emoji[card.identifier] = emojiChoices.remove(at: randomIndex)
        }
        return emoji[card.identifier] ?? "?"
    }
    
    func backgroundColor(for card: Card, at index: Array<Card>.Index) -> UIColor {
       let color = [0, 2, 5, 7, 8, 10, 13, 15].contains(Int(index)) ? #colorLiteral(red: 1, green: 0.6729367971, blue: 0.6634342074, alpha: 1) : #colorLiteral(red: 1, green: 0.667937696, blue: 0.4736554623, alpha: 1)
       return card.isMatched ? #colorLiteral(red: 0.846742928, green: 0.1176741496, blue: 0, alpha: 0) : color
    }
    
    func chooseRandomTheme() -> GameTheme {
        let randomIndex = Int(arc4random_uniform(UInt32(themes.count)))
        return themes[randomIndex]
    }
    
    func resetTheme() {
        currentTheme = chooseRandomTheme()
        emojiChoices = currentTheme.emojis
    }
    
    var themes = [
        GameTheme.init(name: "oldMacDonald", emojis: ["🐷","🐮","🐔","🐰", "🐭", "🐴", "🐱", "🐶", "🐤"]),
        GameTheme.init(name: "underTheSea", emojis: ["🦑","🐋","🐙","🦀", "🐡", "🐟", "🦐", "🐚", "⚓️", "🐠","🐬", "🐳", "🌊", "🚢", "⛴", "🛳", "🦈"]),
        GameTheme.init(name: "natureGarden", emojis: ["🌿","🍄","🌻","🍁", "🌳", "🌱", "🌾", "🌸", "🌞", "🌴", "🍃", "🍂"]),
        GameTheme.init(name: "island", emojis: ["🏝","🌺","🐠","🐬", "⛵️", "🍍", "🍹", "⛱", "🦀", "🥥", "🐢", "👙", "🌋"]),
        GameTheme.init(name: "fruitNinja", emojis: ["🍋","🍉","🍇","🥝", "🥥", "🍑", "🍓", "🍊", "🍐", "🍌", "🍎", "🍏"]),
        GameTheme.init(name: "desertWest", emojis: ["🌵","🏜","🐴","☀️", "🔥", "🍳", "🐍", "💀", "💨"])
    ]
}

struct GameTheme {
    var name: String
    var emojis: [String]
    // could add colors here for the first extra credit item
}

