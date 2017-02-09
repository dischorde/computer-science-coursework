<?php

    // configuration
    require("../includes/config.php");

    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        // render form
        render("add_cash.php", ["title" => "Deposit Cash"]);
    }

    // else if user reached page via POST (as by submitting a form via POST)
    else if ($_SERVER["REQUEST_METHOD"] == "POST")
    {

        // check to ensure deposit value is not empty & a positive number
        if ($_POST["deposit"] <= 0 or empty($_POST["deposit"]))
        {
            apologize("Invalid cash value.");
        }

        // else, update cash
        if ( CS50::query("UPDATE users SET cash = cash + ? WHERE id = ?", $_POST["deposit"],  $_SESSION["id"]) == 0)
        {
            apologize("An error occured! Unable to update cash.");
        }
        
        // redirect
        redirect("/");
        
    }

?>