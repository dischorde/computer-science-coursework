<?php

    // configuration
    require("../includes/config.php");

    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        // get portfolio of stock tickers
        $portfolio = CS50::query("SELECT symbol FROM portfolios WHERE user_id = ?", $_SESSION["id"]); 
        
        // if doesnt have stocks to sell
        if (empty($portfolio))
        {
            apologize("You don't appear to own any stocks.");
        }

        //otherwise, render sell form
        render("sell_form.php", ["title" => "Sell Stock", "tickers" => $portfolio]);
        
    }

    // else if user reached page via POST (as by submitting a form via POST)
    else if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        $shares = CS50::query("SELECT shares FROM portfolios WHERE user_id = ? AND symbol = ?", $_SESSION["id"], $_POST["symbol"]);
        
        // check to ensure that shares > 0 
        if ($shares == 0)
        {
            apologize("An error occured. Cannot sell stocks.");
        }
        
        // look up stock price, calculate total sale price
        $num_shares = $shares[0]["shares"];
        $stock = lookup($_POST["symbol"]);
        $total = $stock["price"] * $num_shares;
        
        // delete shares of that stock from portfolio table
        CS50::query("DELETE FROM portfolios WHERE user_id = ? AND symbol = ?", $_SESSION["id"], $_POST["symbol"]);
        
        // increase cash by amount above
        CS50::query("UPDATE users SET cash = cash + ? WHERE id = ?", $total,  $_SESSION["id"]);
        
        // update history
        CS50::query("INSERT INTO history (user_id, type, timestamp, symbol, shares, price) VALUES(?, 'SELL', NOW(), ?, ?, ?)",
        $_SESSION["id"], $_POST["symbol"], $num_shares, $stock["price"]);
        
        // redirect to portfolio
        redirect("/");
    }

?>