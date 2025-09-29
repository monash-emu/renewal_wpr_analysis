import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime, timedelta

def plot_main(model_data, case_data, mobility_data, vax_data):
    case_index = case_data.index
    cases = case_data
     
    # Define elements needed to add median line plots
    model_index = model_data.index
    weekly_median = model_data["weekly_sum"][0.50]
    rt_median = model_data["R"][0.50]
    suscept_median = model_data["susceptibles"][0.50]
    transmission_median = model_data["transmission potential"][0.50]
    
    
    # Define elements needed for uncertainty plots
    x_vals = model_data.index.to_list() + model_data.index[::-1].to_list()
    y_vals_weekly = model_data["weekly_sum"][0.05].to_list() + model_data["weekly_sum"][0.95][::-1].to_list()
    y_vals_R = model_data["R"][0.05].to_list() + model_data["R"][0.95][::-1].to_list()
    y_vals_suscept = model_data["susceptibles"][0.05].to_list() + model_data["susceptibles"][0.95][::-1].to_list()
    y_vals_transmission = model_data["transmission potential"][0.05].to_list() + model_data["transmission potential"][0.95][::-1].to_list()
    
    # Define elements for mobility plot
    mobility_index = mobility_data.index
    mobility_est = ['transit_stations_percent_change_from_baseline', 'workplaces_percent_change_from_baseline', 'residential_percent_change_from_baseline']
    
    # Define elements for vax plot
    vax_index = vax_data.index
    vax_est = vax_data['people_fully_vaccinated_per_hundred']
                                 
    # Create subplot
    fig = make_subplots(3,2, shared_xaxes=True,  subplot_titles=('a. Reported cases', 'b. Rt', 'c. Susceptible population', 
                                                                 'd. Transmission potential', 'e. Population mobility', 'f. Primary series vaccination coverage'),
                       horizontal_spacing = 0.05, vertical_spacing = 0.05)
    
    # Add modelled case notifications median line
    fig.add_trace(go.Scatter(x=model_index, y=weekly_median, mode="lines", name="Modelled cases", marker_color='#636EFA' ), row=1, col=1)
    # Add modelled case notifications uncertainty
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals_weekly, mode="lines", name="Modelled cases", line={"width": 0.0, "color": '#636EFA'}, fill='toself',
                             showlegend=False ), row=1, col=1)
    # Add case notifications
    fig.add_trace(go.Scatter(x=case_index, y=cases,  mode="markers", name="Reported cases", marker_color="black" ), row=1, col=1)
    
    # Add Rt median line
    fig.add_trace(go.Scatter(x=model_index, y=rt_median, mode="lines", name="Rt", marker_color='#00CC96' ), row=1, col=2)
    # Add Rt uncertainty 
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals_R, mode="lines", name="Rt", line={"width": 0.0, "color": '#00CC96'}, fill='toself', showlegend=False ), row=1,
                  col=2)

    # Add susceptible median line
    fig.add_trace(go.Scatter(x=model_index, y=suscept_median, mode="lines", name="Susceptible", marker_color='#EF553B' ), row=2, col=1)
    # Add susceptible uncertainty 
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals_suscept, mode="lines", name="Susceptible", line={"width": 0.0, "color": '#EF553B'}, fill='toself',
                             showlegend=False ), row=2, col=1)

    # Add transmission potential median line
    fig.add_trace(go.Scatter(x=model_index, y=transmission_median , mode="lines", name="Transmission potential", marker_color='#AB63FA' ), row=2, col=2)
    # Add transmission potential uncerainty 
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals_transmission, mode="lines", name="Transmission potential", line={"width": 0.0, "color": '#AB63FA'},
                             fill='toself', showlegend=False ), row=2, col=2)
    
    # Add mobility figure
    fig.add_trace(go.Scatter(x=mobility_data.index, y=mobility_data['transit_stations_percent_change_from_baseline'], 
                             mode="lines", name="Mobility", line=dict(color='black', dash='dot')), row=3, col=1)
    fig.add_trace(go.Scatter(x=mobility_data.index, y=mobility_data['workplaces_percent_change_from_baseline'], 
                             mode="lines", name="Mobility", line=dict(color='black', dash='dash')), row=3, col=1)
    fig.add_trace(go.Scatter(x=mobility_data.index, y=mobility_data['residential_percent_change_from_baseline'], 
                             mode="lines", name="Mobility", line=dict(color='black')), row=3, col=1)
    # add annotation
    annotat_date = pd.date_range(start="2022-01-01",end="2022-03-01")
    fig.add_trace(go.Scatter(x=annotat_date, y=[i-i-55 for i in range(len(annotat_date))], 
                             mode="lines", line=dict(color='black', dash='dot')), row=3, col=1)
    fig.add_trace(go.Scatter(x=[datetime(2022, 3, 20)], y=[-55], 
                             mode="text", text=['Transit'], line=dict(color='black', dash='dot')), row=3, col=1)
    
    fig.add_trace(go.Scatter(x=annotat_date, y=[i-i-65 for i in range(len(annotat_date))], 
                             mode="lines", text=['Workplaces'], line=dict(color='black', dash='dash')), row=3, col=1)
    fig.add_trace(go.Scatter(x=[datetime(2022, 4, 1)], y=[-65], 
                             mode="text", text=['Workplaces'], line=dict(color='black', dash='dot')), row=3, col=1)
    
    fig.add_trace(go.Scatter(x=annotat_date, y=[i-i-75 for i in range(len(annotat_date))], 
                             mode="lines", text=['Residential'], line=dict(color='black')), row=3, col=1)
    fig.add_trace(go.Scatter(x=[datetime(2022, 4, 1)], y=[-75], 
                             mode="text", text=['Residential'], line=dict(color='black', dash='dot')), row=3, col=1)
    
    # Add vaccination figure
    fig.add_trace(go.Scatter(x=vax_data.index, y=vax_est, mode="lines", name="Vaccination", line={"color": 'black'}), row=3, col=2)
    
                                 
    return fig.update_layout(height=1000, width=1200)                            

