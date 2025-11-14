from shiny import App, ui, render, reactive
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('attendance_anonymised-1.csv')
df_ned = df.drop(columns='Planned End Date')
df_clean = df_ned.rename(columns={'Unit Instance Code': 'Module Code', 'Calocc Code': 'Year','Long Description':'Module Name','Register Event ID':'Event ID','Register Event Slot ID':'Event Slot ID','Planned Start Date':'Date','is Positive':'Has Attended', 'Positive Marks':'Attended','Negative Marks':'NotAttended','Usage Code':'Attendance Code'})
module = 'History'
module_df = df_clean[df_clean['Module Name'] == module]
module_df


app_ui=ui.page_fluid(
ui.output_text("header"),
ui.output_plot("attendance_plot")
)
                   
def server(input, output, session):
     @output
     @render.text                 
     def header():
         return "Attendance Over Time for History Module"
    @output
   
    def attendance_plot():
        fig, ax = plt.subplots()
        ax.plot(module_df['Date'], module_df['NotAttended'])
        ax.set_title('Attendance Over Time for History Module')
        ax.set_xlabel('Date')
        ax.set_ylabel('Not Attended')
        plt.xticks(rotation=45)
        return fig 