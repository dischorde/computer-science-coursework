<?php

    // configuration
    require("../includes/config.php"); 
    // get transactions for history
    $history = [];
    $rows = CS50::query("SELECT * FROM history WHERE user_id = ?", $_SESSION["id"]);
    foreach ($rows as $row)
    {
        $history[] = [
            "type" => $row["type"],
            "datetime" => date('m/j/Y g:i a e' , strtotime($row["timestamp"])),
            "symbol" => $row["symbol"],
            "shares" => $row["shares"],
            "price" => number_format($row["price"], 2),
        ];
    }
    
    // render history
    render("view_history.php", ["title" => "History", "history" => $history]);

?>
