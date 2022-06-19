This is the Natural Computing project on using genetic algorithms to solve blackjack

To run the code, open the "BlackjackStrategy.sln" file with Visual Studio. Running the code within Visual Studio will cause a GUI to pop up. Within the GUI, the desired settings can be selected. Then by pressing the "Find Solution" button, the algorithm will run. It will continue until there are 25 stagnant generations in a row, or it runs for 500 generations. 

At the end, the found solution will be displayed on the GUI. The fitness data from the generations are put into the 'bin/Debug/per-gen-stats.xls' file.

To see the data found over the course of the project, see the 'data' folder. Screenshots of the final solution are saved, as well as the per generation fitness data. The 'plotData.py' script was developed to help process the raw data. The resulting graphs are in the 'processed' folders within the 'data' folder.