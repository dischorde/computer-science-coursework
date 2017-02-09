<form action="sell.php" method="post">
    <fieldset>
        <div class="form-group">
            <select class="form-control" name="symbol">
            <option disabled="" selected="" value="">Choose Stock</option>
            <?php foreach ($tickers as $ticker): ?>
                <option value="<?= $ticker["symbol"] ?>"><?= $ticker["symbol"] ?></option>
            <?php endforeach ?>
            </select>
        </div>
  
        <div class="form-group">
            <button class="btn btn-default" type="submit">
                <span aria-hidden="true" class="glyphicon glyphicon-log-in"></span>
                Sell
            </button>
        </div>
    </fieldset>
</form>