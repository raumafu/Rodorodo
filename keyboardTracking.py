clock_active = False

def start_timer(duration):
    if duration <= 0:
        print("Duration must be a positive integer.")
        return
    
    def toggle_clock_status():
        global clock_active
        clock_active = not clock_active
        
    keyboard.add_hotkey('space', toggle_clock_status)
    
    print(clock_active)
    keyboard.wait('esc')
    