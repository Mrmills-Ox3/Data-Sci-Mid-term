from shiny import App, ui, render, reactive
import pandas as pd
import matplotlib.pyplot as plt

ui=ui.page_fluid(
    ui.output_text("header")
    ui.output_plot("attendance_plot"))    
                   
 def server(input, output, session):
     @render.text("header")                  
)    def header():
            return "Attendance Over Time for History Module"

    @render.plot("attendance_plot")
    def attendance_plot():
        fig, ax = plt.subplots()
        ax.plot(module_df['Date'], module_df['NotAttended'])
        ax.set_title('Attendance Over Time for History Module')
        ax.set_xlabel('Date')
        ax.set_ylabel('Not Attended')
        plt.xticks(rotation=45)
        return fig  