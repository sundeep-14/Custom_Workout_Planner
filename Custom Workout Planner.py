# Custom Workout Planner

def get_user_info():
    print("Welcome to the Custom Workout Planner!")
    name = input("What's your name?:\n ")
    goal = int(input("\n1.weight loss\n2.muscle gain\n3.endurance\nWhat is your fitness goal?: "))
    fitness_level = int(input("\n1.beginner\n2.intermediate\n3.advanced\nWhat is your fitness level?: "))
    days_available = input("\nHow many days per week(1-7) are you available for workouts?:\n ")
    days_available = int(days_available)
    return name, goal, fitness_level, days_available

# Define the workout routine based on user goal and fitness level
def generate_workout_plan(goal, fitness_level, days_available):
    workout_plan = []
    
    if goal == 1:
        if fitness_level == 1:
        
            workout_plan = [
                "Day 1: 30 minutes of cardio (walking, cycling) + 10 minutes of bodyweight exercises (squats, push-ups)",
                "Day 2: Rest or light stretching",
                "Day 3: 30 minutes of cardio + core exercises (planks, crunches)",
                "Day 4: Rest or yoga",
                "Day 5: 30 minutes of cardio + full-body strength exercises",
                "Day 6: Rest or light stretching",
                "Day 7: Outdoor activity (walking, hiking, or swimming)"
            ]
        elif fitness_level == 2:
            workout_plan = [
                "Day 1: 45 minutes of HIIT + bodyweight exercises",
                "Day 2: Rest or yoga",
                "Day 3: 40 minutes of steady cardio + core exercises",
                "Day 4: Upper body strength training",
                "Day 5: 45 minutes of HIIT + full-body workout",
                "Day 6: Rest or yoga",
                "Day 7: Outdoor activity or long cardio session"
            ]
        elif fitness_level == 3:
            workout_plan = [
                "Day 1: 60 minutes of HIIT + strength training",
                "Day 2: Rest or active recovery (light cardio or yoga)",
                "Day 3: 45 minutes of intense cardio + core exercises",
                "Day 4: Upper and lower body strength training",
                "Day 5: 60 minutes of HIIT + full-body workout",
                "Day 6: Rest or active recovery",
                "Day 7: Outdoor activity or long cardio session"
            ]
        else:
            print("Invalid fitness level. Please run the program again and choose 'beginner', 'intermediate', or 'advanced'.")
            return []

    elif goal == 2:
        if fitness_level == 1:
            workout_plan = [
                "Day 1: Full-body workout (squats, push-ups, lunges, dumbbell press)",
                "Day 2: Rest or light stretching",
                "Day 3: Lower body strength workout (squats, lunges, calf raises)",
                "Day 4: Rest or yoga",
                "Day 5: Upper body strength workout (push-ups, rows, shoulder press)",
                "Day 6: Rest or light stretching",
                "Day 7: Outdoor activity (hiking, swimming)"
            ]
        elif fitness_level == 2:
            workout_plan = [
                "Day 1: Upper body strength training (bench press, rows, shoulder press)",
                "Day 2: Rest or yoga",
                "Day 3: Lower body strength training (squats, deadlifts, lunges)",
                "Day 4: Rest or active recovery",
                "Day 5: Full-body workout (squats, deadlifts, bench press)",
                "Day 6: Rest or yoga",
                "Day 7: Outdoor activity or long hike"
            ]
        elif fitness_level == 3:
            workout_plan = [
                "Day 1: Upper body strength training (heavy weights, compound exercises)",
                "Day 2: Rest or active recovery",
                "Day 3: Lower body strength training (heavy squats, deadlifts, lunges)",
                "Day 4: Core workout + cardio",
                "Day 5: Full-body strength training",
                "Day 6: Rest or active recovery",
                "Day 7: Outdoor activity or long cardio session"
            ]
        else:
            print("Invalid fitness level. Please run the program again and choose 'beginner', 'intermediate', or 'advanced'.")
            return []
            
    elif goal == 3:
        if fitness_level == 1:
            workout_plan = [
                "Day 1: Full-body workout (squats, push-ups, lunges, dumbbell press)",
                "Day 2: Rest or light stretching",
                "Day 3: Lower body strength workout (squats, lunges, calf raises)",
                "Day 4: Rest or yoga",
                "Day 5: Upper body strength workout (push-ups, rows, shoulder press)",
                "Day 6: Rest or light stretching",
                "Day 7: Outdoor activity (hiking, swimming)"
            ]
        elif fitness_level == 2:
            workout_plan = [
                "Day 1: Upper body strength training (bench press, rows, shoulder press)",
                "Day 2: Rest or yoga",
                "Day 3: Lower body strength training (squats, deadlifts, lunges)",
                "Day 4: Rest or active recovery",
                "Day 5: Full-body workout (squats, deadlifts, bench press)",
                "Day 6: Rest or yoga",
                "Day 7: Outdoor activity or long hike"
            ]
        elif fitness_level == 3:
            workout_plan = [
                "Day 1: Upper body strength training (heavy weights, compound exercises)",
                "Day 2: Rest or active recovery",
                "Day 3: Lower body strength training (heavy squats, deadlifts, lunges)",
                "Day 4: Core workout + cardio",
                "Day 5: Full-body strength training",
                "Day 6: Rest or active recovery",
                "Day 7: Outdoor activity or long cardio session"
            ]
        else:
            print("Invalid fitness level. Please run the program again and choose 'beginner', 'intermediate', or 'advanced'.")
            return []
    
    else:
        print("Invalid goal. Please run the program again and choose 'weight loss' or 'muscle gain' or 'endurance'.")
        return []

    # Adjust workout plan based on days available
    if days_available < 7:
        workout_plan = workout_plan[:days_available]
        return workout_plan
    
# Function to create a custom workout plan
def workout_planner():
    # Get user inputs for workout
    other_plans = input("\nWould you like to add other workouts in your plan('yes' or 'no')?:\n ")
    if other_plans == "yes" or other_plans == "Yes":
        num_exercises = int(input("\nHow many Would you like to include in your workout?:\n "))
        workout_plan = {}

        for i in range(1, num_exercises + 1):
            exercise_name = input(f"Enter the name of exercise {i}: ")
            num_sets = int(input(f"How many sets for {exercise_name}?: "))
            num_reps = int(input(f"How many reps per set for {exercise_name}?: "))

            # Store the sets and reps for each exercise
            workout_plan[exercise_name] = {'sets': num_sets, 'reps': num_reps}

        # Display the workout plan
        print("\nAdded exercise to your workout plan:")
        for exercise, details in workout_plan.items():
            print(f"{exercise}: {details['sets']} sets of {details['reps']} reps")
        print("\nThank you for visiting our Custom Workout Planner!.")
    else:
        print("\nThank you for visiting our Custom Workout Planner!.")
        return[]

# Main function to run the workout planner
def main():
    name, goal, fitness_level, days_available = get_user_info()
    workout_plan = generate_workout_plan(goal, fitness_level, days_available)

    if workout_plan:
        print(f"\n{name}, here is your custom workout plan for the week based on your goal ({goal}) and fitness level ({fitness_level}):\n")
        for i, workout in enumerate(workout_plan):
            print(f"{workout}")
        workout_planner()

if __name__ == "__main__":
    main()
    

