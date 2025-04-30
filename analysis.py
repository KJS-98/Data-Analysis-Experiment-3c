'''
This code takes reads in a data file where each line represnets a trial and is formatted 
a, b, c. where a=staircase, b=stimulus level and c=response for that trial. It reads this file, and creates 
data in a format compatable with psignifit, while grouping the data into conditions (each one contaning a
1-up, 3-downn and a 3-up, 1-down staircase.  
It then fits a pscyhometric function for each group, and saves the  parameters into a csv file for further 
analyis using statistics software.

It runs one participant at a time, so assuming file names are consistant, you only need to change
the participant number and it will add the data to the existing csv results file. 

There needs to be an existing datafile, and an existing csv file where the data
can be saved. It should have the following headings: 
PNumber,15ms_Threshold,15ms_Width,15ms_Lambda, 15ms_Gamma, 15ms_Eta, 15ms_Slope, 
15ms_Threshold Lower CI, 15ms_Threshold Upper CI, 15ms_Width Lower CI, 
15ms_Width Upper CI, 15ms_Lambda Lower CI, 15ms_Lambda UpperCI, 15ms_Gamma Lower CI, 
15ms_Gamma Upper CI, 15ms_Eta Lower CI, 15ms_Eta Upper CI, 15ms_ThresholdCI_Size, 
15ms_widthCI_Size, 150ms_Threshold, 150ms_Width, 150ms_Lambda, 150ms_Gamma, 150ms_Eta, 
150ms_Slope, 150ms_Threshold Lower CI, 150ms_Threshold Upper CI, 150ms_Width Lower CI, 
150ms_Width Upper CI, 150ms_Lambda Lower CI, 150ms_Lambda Upper CI, 150ms_Gamma Lower CI, 
150ms_Gamma Upper CI, 150ms_Eta Lower CI, 150ms_Eta Upper CI, 150ms_ThresholdCI_Size, 
150ms_widthCI_Size, 2000ms_Threshold, 2000ms_Width, 2000ms_Lambda, 2000ms_Gamma, 2000ms_Eta,
2000ms_Slope, 2000ms_Threshold Lower CI, 2000ms_Threshold Upper CI, 2000ms_Width Lower CI,
2000ms_Width Upper CI, 2000ms_Lambda Lower CI, 2000ms_Lambda Upper CI, 
2000ms_Gamma Lower CI, 2000ms_Gamma Upper CI, 2000ms_Eta Lower CI, 2000ms_Eta Upper CI, 
2000ms_ThresholdCI_Size, 2000ms_widthCI_Size

In the final results csv file, each row will represent a participant. 
'''
import psignifit as ps
import os
import matplotlib.pyplot as plt
import csv

'''
This section of code reads in the data,  groups the data into conditions,
and then changes the format so it is compatable with psignifit.

Here you need to add the correct datafile with raw data in, and also the location
of the csv file where the data will be stored, and the location where the function 
plots will be saved. 

ensure all file names are consistant and in the same locatipn. with the only change 
the participants number. Pnumbers should be 1-15. 
'''
pNumber = 200
while pNumber <= 215: 
        
    showConfIn = True 
    
    dataFile = os.path.join("data", f"P{pNumber}.csv")
    
    plot_folder_path = "output_plots"
    csv_file_path = "analysis_outputs.csv"
    
    #choose options for psignifit based on experimnet type etc. 
    options = dict()
    options['sigmoidName'] = 'neg_gauss'
    options['expType'] = 'YesNo'
    
    # Load the raw data from the .txt" file excluding the last line
    with open(dataFile, 'r') as f:
        raw_data = f.readlines()#[:-1]  # Read all lines except the last one
        raw_data = [line.strip().split(',') for line in raw_data]

    # Group the data by staircase 
    grouped_data = {}
    for staircase, stimulus_level, response in raw_data:
        staircase = float(staircase)
        if staircase in [1, 2, 3, 4]:
            staircase_group = 1 # BB and SS 15ms
        elif staircase in [5, 6, 7, 8]: 
            staircase_group = 2 #BB and SS 150ms 
        elif staircase in [9, 10, 11, 12]:
            staircase_group = 3 #BB and ss 2000ms 
        elif staircase in [13, 14]: 
            staircase_group = 4 #ctrl 15ms
        elif staircase in [15, 16]: 
            staircase_group = 5 #ctrl 150ms   
        elif staircase in [17, 18]: 
            staircase_group = 6 #ctrl 2000ms              
        else:
            raise ValueError(f"Invalid staircase number: {staircase}")
        if staircase_group not in grouped_data:
            grouped_data[staircase_group] = {}
        if stimulus_level not in grouped_data[staircase_group]:
            grouped_data[staircase_group][stimulus_level] = {'total_responses': [], 'num_responses': 0}
        grouped_data[staircase_group][stimulus_level]['total_responses'].append(int(response))
        grouped_data[staircase_group][stimulus_level]['num_responses'] += 1
    
    # Sort the data by stimulus level
    sorted_data = {}
    for staircase, data in grouped_data.items():
        sorted_data[staircase] = sorted(data.items(), key=lambda x: float(x[0]))
    
    # Convert the sorted data to the format needed for psignifit
    psignifit_data = {}
    for staircase, data in sorted_data.items():
        psignifit_data[staircase] = []
        for stimulus_level, responses in data:
            num_ones = sum(1 for r in responses['total_responses'] if r == 1)
            num_trials = responses['num_responses']
            psignifit_data[staircase].append([float(stimulus_level), num_ones, num_trials])
    
    
    '''
    Now this section will fit the functions to the data for each of groups and save 
    them to the file location specified above. It will also extract useful parameters. 
    It calculates out the CI size for threshold and width. 
    It save these parameters to the preexisting csv file. 
    '''
    
    #fit_curve_plots = {}
    
    results_group_1 = []
    results_group_2 = []
    results_group_3 = []
    results_group_4 = []
    results_group_5 = []
    results_group_6 = []    
    
    #for each staircase, get the parameters and CI of these parameters
    for staircase, data in psignifit_data.items():
       
        #get parameters
        results = ps.psignifit(data, options)
        
        
        stairLevel = staircase
        threshold = results['Fit'][0]
        width = results['Fit'][1]
        lambda_param = results['Fit'][2]
        gamma = results['Fit'][3]
        eta = results['Fit'][4]
        slope = ps.getSlopePC(results, 0.5)
        print(slope)
        
        #get upper and lower CI
        conf_intervals_95 = results['conf_Intervals']
        
        ci_low_thresh = conf_intervals_95[0][0, 2]
        ci_up_thresh = conf_intervals_95[0][1, 2]
        ci_low_width = conf_intervals_95[1][0, 2]
        ci_up_width = conf_intervals_95[1][1, 2]
        ci_low_lambda = conf_intervals_95[2][0, 2]
        ci_up_lambda = conf_intervals_95[2][1, 2]
        ci_low_gamma = conf_intervals_95[3][0, 2]
        ci_up_gamma = conf_intervals_95[3][1, 2]
        ci_low_eta = conf_intervals_95[4][0, 2]
        ci_up_eta = conf_intervals_95[4][1, 2]
        
        # Calculate CI sizes
        ci_size_thresh = ci_up_thresh - ci_low_thresh
        ci_size_width = ci_up_width - ci_low_width
    
        # Append the parameters and CI to the appropriate group list
        if staircase == 1:
            condition = '15mTwoOptionss' 
            results_group_1.extend([threshold, width, lambda_param, gamma, eta, slope, 
                                    ci_low_thresh, ci_up_thresh, ci_low_width, ci_up_width, 
                                    ci_low_lambda, ci_up_lambda, ci_low_gamma, ci_up_gamma, 
                                    ci_low_eta, ci_up_eta, ci_size_thresh, ci_size_width])
        elif staircase == 2:
            condition = '150msTwoOptions'
            results_group_2.extend([threshold, width, lambda_param, gamma, eta, slope, 
                                    ci_low_thresh, ci_up_thresh, ci_low_width, ci_up_width, 
                                    ci_low_lambda, ci_up_lambda, ci_low_gamma, ci_up_gamma, 
                                    ci_low_eta, ci_up_eta, ci_size_thresh, ci_size_width])
        elif staircase == 3:
            condition = '2000msTwoOptions'
            results_group_3.extend([threshold, width, lambda_param, gamma, eta, slope, 
                                    ci_low_thresh, ci_up_thresh, ci_low_width, ci_up_width, 
                                    ci_low_lambda, ci_up_lambda, ci_low_gamma, ci_up_gamma, 
                                    ci_low_eta, ci_up_eta, ci_size_thresh, ci_size_width])
        elif staircase == 4:
            condition = 'ctrl_15msOneOption'
            results_group_4.extend([threshold, width, lambda_param, gamma, eta, slope, 
                                    ci_low_thresh, ci_up_thresh, ci_low_width, ci_up_width, 
                                    ci_low_lambda, ci_up_lambda, ci_low_gamma, ci_up_gamma, 
                                    ci_low_eta, ci_up_eta, ci_size_thresh, ci_size_width])        
        elif staircase == 5:
            condition = 'ctrl_150msOneOption'
            results_group_5.extend([threshold, width, lambda_param, gamma, eta, slope, 
                                    ci_low_thresh, ci_up_thresh, ci_low_width, ci_up_width, 
                                    ci_low_lambda, ci_up_lambda, ci_low_gamma, ci_up_gamma, 
                                    ci_low_eta, ci_up_eta, ci_size_thresh, ci_size_width])
        elif staircase == 6:
            condition = 'ctrl_2000msOneOption'
            results_group_6.extend([threshold, width, lambda_param, gamma, eta, slope, 
                                    ci_low_thresh, ci_up_thresh, ci_low_width, ci_up_width, 
                                    ci_low_lambda, ci_up_lambda, ci_low_gamma, ci_up_gamma, 
                                    ci_low_eta, ci_up_eta, ci_size_thresh, ci_size_width]) 
        
        min_x = 0
        max_x = 250
        #Fit plots for each staircase, then save them. 
        fit_curve_plot = ps.psigniplot.plotPsych(results, showImediate=True, plotThresh = True, yLabel = 'proportion judged stepable', xLabel = 'diameter (mm)', CIthresh = showConfIn )
        plt.ylim(-2, 2)
        plt.xlim(0,10)
        axes = fit_curve_plot.figure.axes[0]  # Access the first (and likely only) axes object
        axes.set_xlim(min_x, max_x)  # Explicitly set x-axis limits

        # Save the figure
        plot_file_path = os.path.join(plot_folder_path, f"Participant{pNumber}_{condition}.png")
        fit_curve_plot.figure.savefig(plot_file_path)
        print("Plot saved:", plot_file_path)

        plt.close(fit_curve_plot.figure)  # Close the figure
        
    '''    
    # Open the CSV file for writing
    with open(csv_file_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
    
        # Append the data to the existing CSV file as a single row
        csv_writer.writerow([pNumber] + results_group_1 + results_group_2 + results_group_3 + results_group_4 + results_group_5 + results_group_6 )
    '''
    pNumber = pNumber + 1
        
    
        
