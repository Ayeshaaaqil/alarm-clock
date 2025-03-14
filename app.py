import streamlit as st
import time
from datetime import datetime, timedelta
import threading

# Set page title and configuration
st.set_page_config(page_title="Streamlit Alarm Clock", page_icon="⏰")
st.title("⏰ Streamlit Alarm Clock")

# Initialize session state variables if they don't exist
if 'alarm_time' not in st.session_state:
    st.session_state.alarm_time = None
if 'alarm_set' not in st.session_state:
    st.session_state.alarm_set = False
if 'alarm_triggered' not in st.session_state:
    st.session_state.alarm_triggered = False

# Function to check if alarm should go off
def check_alarm():
    while st.session_state.alarm_set:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == st.session_state.alarm_time and not st.session_state.alarm_triggered:
            st.session_state.alarm_triggered = True
            # In a real application, you would play a sound here
            print(f"⏰ ALARM! It's {current_time}!")
            break
        time.sleep(1)

# Display current time
current_time = datetime.now().strftime("%H:%M:%S")
st.subheader(f"Current Time: {current_time}")

# Create two columns for hour and minute selection
col1, col2 = st.columns(2)

with col1:
    hour = st.selectbox("Hour", range(24), index=datetime.now().hour)
    
with col2:
    minute = st.selectbox("Minute", range(60), index=datetime.now().minute)

# Format the selected time
selected_time = f"{hour:02d}:{minute:02d}"

# Set alarm button
if st.button("Set Alarm"):
    st.session_state.alarm_time = selected_time
    st.session_state.alarm_set = True
    st.session_state.alarm_triggered = False
    
    # Start the alarm checking thread (note: this is simulated in this environment)
    # In a real application, you would use threading.Thread(target=check_alarm).start()
    st.success(f"Alarm set for {selected_time}")
    
    # For demonstration purposes, we'll simulate the alarm check
    current_time = datetime.now().strftime("%H:%M")
    if current_time == selected_time:
        st.session_state.alarm_triggered = True
        st.error("⏰ ALARM! Time to wake up!")
    else:
        # Calculate time difference for demonstration
        now = datetime.now()
        alarm_datetime = datetime(now.year, now.month, now.day, hour, minute)
        if alarm_datetime < now:  # If alarm time is earlier today, it's for tomorrow
            alarm_datetime += timedelta(days=1)
        time_diff = alarm_datetime - now
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        st.info(f"Alarm will go off in {hours} hours, {minutes} minutes, and {seconds} seconds")

# Display alarm status
if st.session_state.alarm_set:
    st.write(f"Alarm is set for: {st.session_state.alarm_time}")
    
    # Button to stop the alarm
    if st.button("Stop Alarm"):
        st.session_state.alarm_set = False
        st.session_state.alarm_triggered = False
        st.success("Alarm stopped")

# Display alarm notification if triggered
if st.session_state.alarm_triggered:
    st.error("⏰ ALARM! Time to wake up!")
    
    # Add a snooze button
    if st.button("Snooze (5 minutes)"):
        now = datetime.now()
        snooze_time = now + timedelta(minutes=5)
        st.session_state.alarm_time = snooze_time.strftime("%H:%M")
        st.session_state.alarm_triggered = False
        st.info(f"Alarm snoozed until {st.session_state.alarm_time}")

# Note about the demo
st.markdown("---")
st.info("""
**Note:** This is a demonstration of a Streamlit alarm clock. In this environment, 
the alarm won't actually play a sound, and the continuous time checking is simulated. 
In a real application, you would:
1. Use threading to check the time continuously
2. Play a sound when the alarm triggers
3. Implement persistent storage for alarms
""")

# Display instructions for running locally
st.markdown("---")
st.subheader("How to run this locally:")
st.code("""
# 1. Save this code as alarm_clock.py
# 2. Install streamlit: pip install streamlit
# 3. Run the app: streamlit run alarm_clock.py
""")

# For demonstration purposes, simulate the passage of time
print(f"Current time: {current_time}")
if st.session_state.alarm_set:
    print(f"Alarm set for: {st.session_state.alarm_time}")