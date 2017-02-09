<?php

    // configuration
    require("../includes/config.php");

    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        // render form
        render("buy_form.php", ["title" => "Buy Stocks"]);
    }

    // else if user reached page via POST (as by submitting a form via POST)
    else if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        
        // check to ensure symbol is not empty
        if (empty($_POST["symbol"]))
        {
            apologize("You must enter a ticker symbol.");
        }
        
        // check to ensure stock is not empty & a whole number
        if (!preg_match("/^\d+$/", $_POST["shares"]) or empty($_POST["shares"]))
        {
            apologize("Invalid number of shares.");
        }
        
        // else, lookup 
        $stock = lookup($_POST["symbol"]);
        $total_price = $stock["price"] * $_POST["shares"];
        
        // ensure symbol was valid
        if ($stock == false)
        {
            apologize("Invalid ticker symbol");
        }
        
        // lookup cash on hand
        $rows =  CS50::query("SELECT cash FROM users WHERE id = ?", $_SESSION["id"]); 
        
        // if stock is too expensive, apologize
        if ($rows[0]["cash"] < $total_price)
        {
            apologize("You do not have enough money for this purchase.");
        }
        
        // else, decrement cash by total price
        CS50::query("UPDATE users SET cash = cash - ? WHERE id = ?", $total_price,  $_SESSION["id"]);
        
        // add stock to portfolio
        CS50::query("INSERT INTO portfolios (user_id, symbol, shares) VALUES(?, ?, ?) ON DUPLICATE KEY UPDATE shares = shares + VALUES(shares)", 
        $_SESSION["id"], strtoupper($_POST["symbol"]), $_POST["shares"]);
        
        // update history
        CS50::query("INSERT INTO history (user_id, type, timestamp, symbol, shares, price) VALUES(?, 'BUY', NOW(), ?, ?, ?)",
        $_SESSION["id"], strtoupper($_POST["symbol"]), $_POST["shares"], $stock["price"]);
        
        // redirect
        redirect("/");
        
    }

?>