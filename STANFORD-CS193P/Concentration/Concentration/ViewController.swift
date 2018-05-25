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
    
    @IBOutlet weak var newGameButton: UIButton!
    
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
    
    override func viewDidLoad() {
        self.view.backgroundColor = currentTheme.backgroundColor
        newGameButton.backgroundColor = currentTheme.primaryColor
        updateViewFromModel()
    }
    
    func updateViewFromModel() {
        flipCountLabel.text = "Flips: \(game.flipCount)"
        scoreLabel.text = "Score: \(game.score)"
        self.view.backgroundColor = currentTheme.backgroundColor
         newGameButton.backgroundColor = currentTheme.primaryColor
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
       let color = [0, 2, 5, 7, 8, 10, 13, 15].contains(Int(index)) ? currentTheme.primaryColor : currentTheme.accentColor
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
        GameTheme.init(name: "oldMacDonald", emojis: ["🐷","🐮","🐔","🐰", "🐭", "🐴", "🐱", "🐶", "🐤"], backgroundColor: #colorLiteral(red: 0.8374180198, green: 0.8374378085, blue: 0.8374271393, alpha: 1), primaryColor: #colorLiteral(red: 0.4620226622, green: 0.8382837176, blue: 1, alpha: 1), accentColor: #colorLiteral(red: 0.9999960065, green: 1, blue: 1, alpha: 1)),
        GameTheme.init(name: "underTheSea", emojis: ["🦑","🐋","🐙","🦀", "🐡", "🐟", "🦐", "🐚", "⚓️", "🐠","🐬", "🐳", "🌊", "🚢", "⛴", "🛳", "🦈"], backgroundColor: #colorLiteral(red: 0, green: 0.2684682608, blue: 0.4762560725, alpha: 1), primaryColor:#colorLiteral(red: 0.4699950814, green: 0.6678406, blue: 0.8381099105, alpha: 1), accentColor: #colorLiteral(red: 0.2199882269, green: 0.8307816982, blue: 0.8380283117, alpha: 1)),
        GameTheme.init(name: "natureGarden", emojis: ["🌿","🍄","🌻","🍁", "🌳", "🌱", "🌾", "🌸", "🌞", "🌴", "🍃", "🍂"], backgroundColor: #colorLiteral(red: 0.2516767979, green: 0.4673609138, blue: 0.2600513697, alpha: 1), primaryColor:#colorLiteral(red: 0.4690613151, green: 0.6526823044, blue: 0.2587630153, alpha: 1), accentColor: #colorLiteral(red: 0.4692698717, green: 0.6561034322, blue: 0.4752988815, alpha: 1)),
        GameTheme.init(name: "island", emojis: ["🏝","🌺","🐠","🐬", "⛵️", "🍍", "🍹", "⛱", "🦀", "🥥", "🐢", "👙", "🌋"], backgroundColor: #colorLiteral(red: 0.6590628028, green: 0.8345142603, blue: 0.8376920223, alpha: 1), primaryColor: #colorLiteral(red: 1, green: 0.6729367971, blue: 0.6634342074, alpha: 1), accentColor: #colorLiteral(red: 1, green: 0.667937696, blue: 0.4736554623, alpha: 1)),
        GameTheme.init(name: "fruitNinja", emojis: ["🍋","🍉","🍇","🥝", "🥥", "🍑", "🍓", "🍊", "🍐", "🍌", "🍎", "🍏"], backgroundColor: #colorLiteral(red: 0.8412034512, green: 0.6681704521, blue: 0.6638730168, alpha: 1), primaryColor: #colorLiteral(red: 0.8459790349, green: 0.2873021364, blue: 0.2579272389, alpha: 1), accentColor: #colorLiteral(red: 0.8467822075, green: 0.127263248, blue: 0.2581181526, alpha: 1)),
        GameTheme.init(name: "desertWest", emojis: ["🌵","🏜","🐴","☀️", "🔥", "🍳", "🐍", "💀", "💨"], backgroundColor: #colorLiteral(red: 1, green: 0.8323456645, blue: 0.4732058644, alpha: 1), primaryColor: #colorLiteral(red: 1, green: 0.4883337617, blue: 0.2560397685, alpha: 1), accentColor: #colorLiteral(red: 0.8409169316, green: 0.6583849192, blue: 0, alpha: 1)),
    ]
}

struct GameTheme {
    var name: String
    var emojis: [String]
    var backgroundColor: UIColor
    var primaryColor: UIColor
    var accentColor: UIColor
}

