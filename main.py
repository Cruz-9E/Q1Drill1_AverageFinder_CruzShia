from pyscript import display, document
def average_score(event): 
    score1 = int(document.getElementById("input1").value)
    score2 = int(document.getElementById("input2").value)
   
    average = int((score1 + score2)/2) # This makes it so that the average rounds off, not giving a floating point
    passing_score = 75
    
    if average >= passing_score: # Setting up the equation to check whether they passed or failed.
        status = "Passed"
    else:
        status = "Failed"
        
    display(f"Average: {average}", target="output1")
    display(status, target = "output2")