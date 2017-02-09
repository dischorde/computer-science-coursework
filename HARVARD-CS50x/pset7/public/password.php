<?php

    // configuration
    require("../includes/config.php"); 

    // if user reached page via GET (as by clicking a link or via redirect)
    if ($_SERVER["REQUEST_METHOD"] == "GET")
    {
        // else render form
        render("change_pass.php", ["title" => "Change Password"]);
    }

    // else if user reached page via POST (as by submitting a form via POST)
    else if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // confirm old and new passwords are not empty
        if (empty($_POST["password"]))
        {
            apologize("You must provide your current password.");
        }
        
        else if (empty($_POST["newpass"]))
        {
            apologize("Invalid new password.");
        }
        
        // ensure password and password confirmation match
        else if ($_POST["newpass"] != $_POST["confirmation"])
        {
            apologize("Passwords do not match.");
        }

        // query database for user
        $rows = CS50::query("SELECT hash FROM users WHERE id = ?",  $_SESSION["id"]);

        // first (and only) row
        $row = $rows[0];

        // compare hash of user's input against hash that's in database
        if (!password_verify($_POST["password"], $row["hash"]))
        {
            apologize("Current Password Incorrect - Could Not Change.");     
        }

        // else change
        if (CS50::query("UPDATE users SET hash = ? WHERE id = ?", password_hash($_POST["newpass"], PASSWORD_DEFAULT),  $_SESSION["id"]) == false)   
        {
            apologize("An error occured. Could not change password.");
        }
        else
        {
            redirect("/");
        }
    }

?>



        
        