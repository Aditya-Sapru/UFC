import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="UFC 317: Topuria vs Oliveira",
    page_icon="🥊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    }
    
    .title-container {
        background: linear-gradient(45deg, #ff6b35, #f7931e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        padding: 20px 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #ff6b35, #f7931e);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
        color: white;
        margin: 10px 0;
    }
    
    .fight-result {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
        border-left: 4px solid #ff6b35;
        color: white;
    }
    
    .fighter-name {
        color: #ff6b35;
        font-weight: bold;
    }
    
    .result-method {
        color: #4CAF50;
        font-weight: bold;
    }
    
    .ko-result { border-left-color: #e74c3c !important; }
    .sub-result { border-left-color: #9b59b6 !important; }
    .dec-result { border-left-color: #3498db !important; }
    
    h1, h2, h3 {
        color: #ff6b35 !important;
    }
    
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Title and header
st.markdown('<div class="title-container">', unsafe_allow_html=True)
st.title("🥊 UFC 317: TOPURIA VS OLIVEIRA")
st.markdown("**Complete Fight Statistics & Analysis | June 28, 2025 | T-Mobile Arena, Las Vegas**")
st.markdown('</div>', unsafe_allow_html=True)

# Summary statistics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Fights", "11", help="Total number of fights on the card")
    
with col2:
    st.metric("Finishes", "7", help="Fights ending by KO or submission")
    
with col3:
    st.metric("Finish Rate", "64%", help="Percentage of fights ending in finishes")
    
with col4:
    st.metric("Fastest KO", "2:27", help="Topuria's knockout of Oliveira")

st.markdown("---")

# Fight data
fight_data = {
    'Fighter': ['Ilia Topuria', 'Alexandre Pantoja', 'Joshua Van', 'Beneil Dariush', 'Payton Talbott',
                'Gregory Rodrigues', 'Jose Miguel Delgado', 'Tracy Cortez', 'Terrance McKinney', 
                'Jacobe Smith', 'Jhonata Diniz'],
    'Opponent': ['Charles Oliveira', 'Kai Kara-France', 'Brandon Royval', 'Renato Moicano', 'Felipe Lima',
                 'Jack Hermansson', 'Hyder Amil', 'Viviane Araújo', 'Viacheslav Borshchev',
                 'Niko Price', 'Alvin Hines'],
    'Result': ['Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win'],
    'Method': ['KO', 'SUB', 'DEC', 'DEC', 'DEC', 'KO', 'KO', 'DEC', 'SUB', 'SUB', 'DEC'],
    'Round': [1, 3, 3, 3, 3, 1, 1, 3, 1, 2, 3],
    'Time': ['2:27', '1:55', '5:00', '5:00', '5:00', '4:21', '0:26', '5:00', '0:55', '4:03', '5:00'],
    'Weight_Class': ['Lightweight', 'Flyweight', 'Flyweight', 'Lightweight', 'Bantamweight',
                     'Middleweight', 'Heavyweight', "Women's Flyweight", 'Lightweight', 'Welterweight', 'Heavyweight'],
    'Card_Position': ['Main', 'Main', 'Main', 'Main', 'Main', 'Prelim', 'Prelim', 'Prelim', 'Prelim', 'Prelim', 'Prelim']
}

df = pd.DataFrame(fight_data)

# Create two columns for charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Fight Outcomes Distribution")
    
    # Pie chart for outcomes
    outcome_counts = df['Method'].value_counts()
    colors = ['#e74c3c', '#9b59b6', '#3498db']
    
    fig_pie = go.Figure(data=[go.Pie(
        labels=outcome_counts.index,
        values=outcome_counts.values,
        hole=0.4,
        marker_colors=colors,
        textinfo='label+percent',
        textfont_size=12
    )])
    
    fig_pie.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=True,
        height=400
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.subheader("⚡ Finish Methods Breakdown")
    
    # Bar chart for finish methods
    finish_methods = ['Right Hook KO', 'Left Hook KO', 'Strikes KO', 'RNC Sub', 'Guillotine Sub']
    finish_counts = [2, 1, 1, 2, 1]
    colors_bar = ['#ff6b35', '#e74c3c', '#c0392b', '#9b59b6', '#8e44ad']
    
    fig_bar = go.Figure(data=[go.Bar(
        x=finish_methods,
        y=finish_counts,
        marker_color=colors_bar,
        text=finish_counts,
        textposition='auto'
    )])
    
    fig_bar.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        yaxis_title='Frequency',
        xaxis_title='Finish Method',
        height=400
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)

# Second row of charts
col3, col4 = st.columns(2)

with col3:
    st.subheader("🏆 Weight Class Performance")
    
    # Weight class analysis
    weight_class_data = df.groupby('Weight_Class').agg({
        'Method': lambda x: (x != 'DEC').sum() / len(x) * 100
    }).round(1)
    
    fig_radar = go.Figure()
    
    fig_radar.add_trace(go.Scatterpolar(
        r=weight_class_data['Method'].values,
        theta=weight_class_data.index,
        fill='toself',
        name='Finish Rate %',
        line_color='#ff6b35',
        fillcolor='rgba(255, 107, 53, 0.3)'
    ))
    
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                color='white'
            ),
            angularaxis=dict(color='white')
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=400
    )
    
    st.plotly_chart(fig_radar, use_container_width=True)

with col4:
    st.subheader("⏱️ Fight Duration Analysis")
    
    # Duration analysis
    duration_data = df.groupby('Round').size().reset_index(name='count')
    duration_labels = ['Round 1', 'Round 2', 'Round 3']
    duration_counts = [duration_data[duration_data['Round']==i]['count'].values[0] if i in duration_data['Round'].values else 0 for i in [1,2,3]]
    
    fig_line = go.Figure()
    
    fig_line.add_trace(go.Scatter(
        x=duration_labels,
        y=duration_counts,
        mode='lines+markers',
        line=dict(color='#ff6b35', width=4),
        marker=dict(size=12, color='#ff6b35'),
        fill='tonexty',
        fillcolor='rgba(255, 107, 53, 0.3)',
        name='Fights Ending'
    ))
    
    fig_line.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        yaxis_title='Number of Fights',
        xaxis_title='Round',
        height=400
    )
    
    st.plotly_chart(fig_line, use_container_width=True)

# Third row of charts
col5, col6 = st.columns(2)

with col5:
    st.subheader("📺 Main Card vs Prelims")
    
    # Card comparison
    card_analysis = df.groupby(['Card_Position', 'Method']).size().unstack(fill_value=0)
    
    fig_stack = go.Figure()
    
    colors_stack = {'KO': '#e74c3c', 'SUB': '#9b59b6', 'DEC': '#3498db'}
    
    for method in card_analysis.columns:
        fig_stack.add_trace(go.Bar(
            name=method,
            x=card_analysis.index,
            y=card_analysis[method],
            marker_color=colors_stack.get(method, '#ffffff')
        ))
    
    fig_stack.update_layout(
        barmode='stack',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        yaxis_title='Number of Fights',
        xaxis_title='Card Position',
        height=400
    )
    
    st.plotly_chart(fig_stack, use_container_width=True)

with col6:
    st.subheader("🌟 Fighter Experience Levels")
    
    # Experience levels (synthetic data based on fight analysis)
    experience_data = {
        'Level': ['Champions', 'Former Champions', 'Contenders', 'Rising Prospects', 'Veterans'],
        'Count': [1, 2, 4, 3, 2]
    }
    
    fig_polar = go.Figure()
    
    colors_polar = ['#f1c40f', '#e67e22', '#e74c3c', '#2ecc71', '#9b59b6']
    
    fig_polar.add_trace(go.Barpolar(
        r=experience_data['Count'],
        theta=experience_data['Level'],
        marker_color=colors_polar,
        marker_line_color='black',
        marker_line_width=2,
        opacity=0.8
    ))
    
    fig_polar.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 5], color='white'),
            angularaxis=dict(color='white')
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=400
    )
    
    st.plotly_chart(fig_polar, use_container_width=True)

st.markdown("---")

# Main Card Results Section
st.subheader("🏆 Main Card Results")

main_card_results = [
    ("Ilia Topuria", "Charles Oliveira", "KO (Right Hook) - R1 2:27", "ko"),
    ("Alexandre Pantoja", "Kai Kara-France", "SUB (RNC) - R3 1:55", "sub"),
    ("Joshua Van", "Brandon Royval", "UD (29-28, 29-28, 30-27)", "dec"),
    ("Beneil Dariush", "Renato Moicano", "UD (29-28, 29-28, 29-28)", "dec"),
    ("Payton Talbott", "Felipe Lima", "UD (29-28, 29-28, 29-28)", "dec")
]

for winner, loser, method, result_type in main_card_results:
    st.markdown(f"""
    <div class="fight-result {result_type}-result">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <span class="fighter-name">{winner}</span> defeats {loser}
            </div>
            <div class="result-method">{method}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Data table
st.markdown("---")
st.subheader("📋 Complete Fight Data")

# Style the dataframe
styled_df = df.style.set_properties(**{
    'background-color': 'rgba(255, 255, 255, 0.05)',
    'color': 'white',
    'border-color': 'rgba(255, 255, 255, 0.1)'
})

st.dataframe(df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888; padding: 20px;'>"
    "UFC 317: Topuria vs Oliveira Statistics Dashboard | Built with Streamlit & Plotly"
    "</div>", 
    unsafe_allow_html=True
)