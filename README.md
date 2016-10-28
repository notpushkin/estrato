# estrato
A REPL to interact with an Electrum / Stratum server.

```bash
$ pipsi install --python python3.5 estrato
$ estrato 
Connected to: cluelessperson.com
  ___  __    __  __  ____  __    ____  ___  ___  ____  ____  ____  ___  _____  _  _ 
 / __)(  )  (  )(  )( ___)(  )  ( ___)/ __)/ __)(  _ \( ___)(  _ \/ __)(  _  )( \( )
( (__  )(__  )(__)(  )__)  )(__  )__) \__ \\__ \ )___/ )__)  )   /\__ \ )(_)(  )  ( 
 \___)(____)(______)(____)(____)(____)(___/(___/(__)  (____)(_)\_)(___/(_____)(_)\_)

>>> server.donation_address
'1LN1Si4hsx7BHTed4KNHorUKjdBzjXsTKj'

>>> blockchain.address.get_balance '1LN1Si4hsx7BHTed4KNHorUKjdBzjXsTKj'
{'unconfirmed': 0, 'confirmed': 100000}
```
