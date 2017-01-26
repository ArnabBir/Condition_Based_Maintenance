# Condition_Based_Maintenance

##Remaining Useful Life Prediction Challenge

###Remaining Useful Life
Prognostics is a dynamic process that evolves in time from the moment the machine is first used until it fails. Remaining Useful Life (RUL) should not be confused with expected life expectancy, which is the “mean-time-to-failure” of an average machine/component. Expected life expectancy is the average life of similar components/machines or a family of machines, while RUL is the time-to-failure of a specific machine, which is being monitored.

###Experimental Setup
Drilling process, one of the most commonly used machining processes, is selected here as a test-bed for validating the proposed autonomous diagnostics framework. The objective is to predict the RUL drill-bit during the machining process by utilizing thrust-force and torque signals captured by a dynamometer during the drilling cycle (constituting a logical sensor signal segment). Tests were conducted on HAAS VF-1 CNC Machining Center with Kistler 9257B piezo-dynamometer (sampled at 250Hz) to drill holes in ¼ inch stainless steel bars. High-speed twist drill-bits with two flutes were operated at feed rate of 4.5 inch/minute and spindle-speed at 800 rpm without coolant. Each drill-bit was used until it reached a state of physical failure either due to excessive wear or due to gross plastic deformation of the tool tip due to excessive temperature (resulting from excessive wear).
###Data
Data is provided as a mat file (MATLAB). Once, you load this in the workspace, you can see many arrays with names such as ‘d1h1’ representing drill bit 1, hole 1. All together there are 14 drill bit with varying number of holes drilled. You are expected to predict the remaining-useful-life (RUL). In terms of data, RUL can be understood as follows: Let’s consider Drill bit 1. It has drilled 19 holes before failure. So, when it is drilling 4th hole we can calculate actual RUL (before it fails) as 19-4 = 15. Now, your task is to build a prediction model that can predict RUL in the real life. You can divide this dataset as first 10 drill bits and last 4 drill bits for training and testing respectively.

###Performance criteria
Median RMSE for testing dataset made up of just the last five holes for each drill bit. Whereas, error can be calculated as = (Actual RUL – Estimated RUL).

###Reference
Kumar, A., Tseng, F., Guo, Y., and Chinnam, R. B., (2008) “Hidden-Markov Model Based Sequential Clustering for Autonomous Diagnostics,” Proc. of IEEE International Joint Conference on Neural Networks (IJCNN), Hong Kong, June 1-6, 2008.
