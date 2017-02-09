<?php

    require(__DIR__ . "/../includes/config.php");

    // numerically indexed array of places
    $places = [];

    // Search database for places matching $_GET["geo"], store in $places
    $places = CS50::query("SELECT * FROM places WHERE MATCH (postal_code, place_name, admin_code1, admin_name1) AGAINST (?)", $_GET["geo"]);
    
    if ($places == [])
    {
        // check to see if is a state code
        $places = CS50::query("SELECT * FROM places WHERE (admin_code1) LIKE (?)", $_GET["geo"]);
        
        // if nothing comes up, try wildcard 
        if ($places == [])
        {
            $places = CS50::query("SELECT * FROM places WHERE MATCH (postal_code, place_name, admin_code1, admin_name1) AGAINST (? IN BOOLEAN MODE)", $_GET["geo"] . "*");
        }
    }    
        
    // output places as JSON (pretty-printed for debugging convenience)
    header("Content-type: application/json");
    print(json_encode($places, JSON_PRETTY_PRINT));

?>