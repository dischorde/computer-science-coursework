<?php

    // configuration
    require("../includes/config.php");

    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        // render form
        render("search_quote.php", ["title" => "Quote"]);
    }

    // else if user reached page via POST (as by submitting a form via POST)
    else if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        
        // check to ensure symbol is not empty
        if (empty($_POST["symbol"]))
        {
            apologize("You must enter a ticker symbol.");
        }
        
        // else, lookup 
        $stock = lookup($_POST["symbol"]);
        
        // ensure symbol was valid
        if ($stock == false)
        {
            apologize("Invalid ticker symbol");
        }
        
        $rounded = number_format($stock["price"], 2);
        
        render("show_quote.php", ["title" => "Quote", "price" => $rounded, "name" => $stock["name"], "symbol" => $stock["symbol"] ]);        
    }

?>