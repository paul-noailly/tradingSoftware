# strategy_software


> :warning: **Old Project**: No longer suported 

This project consists on a software, built with pyqt5.
Similar to trading view, with unlimited indicators, but no live data, it will provide a plateform to:
- import all kind of data in a csv format (check boxes for what to plot and how to plot) (req. = timestamp columns)
- plot price in an interactive chart windows using plotly
- show all kind of built in indicators
- build indicators (input the equation and save it, no code)
- build strategy (fill entryLong, exitLong, entryShort, exitShort conditions joined by 'and' and 'or', and conditioning of filling, fees, ect..)
- backtest strategy (use task? because it might take long)
- link trading account to the plateform (via api key) and see funds and summary
- push a strategy on a linked accound to generate the trading code (and launch the google instance?)
- labelling: generate list of key point of interest (ex: reversal points) by clicking on the chart.
- ds: supported tools for data science. (behavior of data around reversals, of behavior of windowed data around key points of interest + data visualisation)
- ml: possibility to run ml (ex: xgboost model) on the generated labelisation
- dl: possibility to run adjusted deep learning (cnn) models on data behavior around key point of interest

Backtesting:
-multi markets/mono market
-accurate (tick) / signal return


### PyQt5 designer
preview: ```ctrl+r```

other:

### How to modify the software

- Add Indicator:
  - Go to `indicatorGenerator.py` build the function to build the outputs dictionary
  - Add this function call to the get_outputs_array
  - Then go in the file indicator/indicator.json and add the details of the indicator in it (default config, main and sub group, inputs, params default params and config builder)
  - If the config builder call a new type of config, then add it to the file `dialog_adaptativeConfig` in the setup ui loop.

### Todo List
- [x] Faire le constucteur du standard_plot_item (similaire au ohlc plot item) puis le rajoute au plotData
- [x] Regler le bug  qui affiche 4 dialog config variables
- [x] fixer le bug du condlestick painter
- [x] connecter les check boxes var aux config plot
- [x] Dans le dic_work, puis variables, puis config: rajouter une key data_modif. qui prend les valeurs:
  - [x] 'original' x(t)
  - [x] 'diff from 1st' ( x(t) - x(0) ) / x(0)
  - [x] 'diff from previous'
  - [x] 'diff from average (p)'
- [ ] Rajouter une façon de créer des nouveau docks.
  - [ ] rajouter la fonction dans les dialog edit config
  - [ ] rajouter le constructeur + placement des docks au call de plot_data
  - [ ] rajouter l'interpréteur de positionement
- [x] faire la fonction create indicator: (CANCELED)
  - [x] via formule mathématique, select nbs input, + pick name for inputs.
  - [x] Construit la formule + nbs output + name output
  - [x] construit l'editeur de config + plot (ex cas particulier bollinger)
- [ ] Rajouter le add variable avec 2 mode:
  - [x] add indicateur (en attachant les noms des input à des variables dispo)
  - [ ] add data qui va pick dans les imported data de nouvelles data
  - [ ] import indicator lframework: set d'indicator (précédement sauvegarder) et applicable dirrectement aux data. Pour cela dans le dic_sumup.vaiables.var de types indicator, rajouter le constructeur ectt..
- [ ] Constuire le modificateur de timeframe 2 possibilité:
  - [ ] dans config, dès qu'un tf est choisi, resample la data si pas deja faite et plot
  - [ ] dans config, option de créer un tf, qui resamble, pluis on peut selectionner le t
- [ ] Constuire le createur de strategie avec 2 modes:
  - [ ] Le mod unimarket
  - [ ] le mode polymarket (ex: scalping all forex pair)
  - [ ] rajouter le pot signal
  - [x] rajouter le labelling?
- [x] Revoir l'import et la creation de new work afin de considérer l'ohlc comme un indicateur plutot qu'une data
- [ ] Concevoir la labellisation
  - [x] faire la structure sur papier
  - [ ] créer les dialog generator
  - [ ] gérer l'exportation
  - [ ] faire un code sur notebook pour analyse statistique des indicateur pre-label
