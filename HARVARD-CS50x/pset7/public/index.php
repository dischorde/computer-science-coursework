<?php

    // configuration
    require("../includes/config.php"); 

    // get stock prices etc. for porfolio
    $positions = [];
    $rows = CS50::query("SELECT symbol, shares FROM portfolios WHERE user_id = ?", $_SESSION["id"]);
    foreach ($rows as $row)
    {
        $stock = lookup($row["symbol"]);
        if ($stock !== false)
        {
            $positions[] = [
                "name" => $stock["name"],
                "price" => $stock["price"],
                "shares" => $row["shares"],
                "symbol" => $row["symbol"],
                "total" => number_format($stock["price"] * $row["shares"], 2),
            ];
        }
    }
    
    // get cash total remaining
    $users = CS50::query("SELECT cash FROM users WHERE id = ?", $_SESSION["id"]);
    $cash = number_format($users[0]["cash"], 2);
    
    // render portfolio
    render("portfolio.php", ["title" => "Portfolio", "positions" => $positions, "cash" => $cash]);

?>
