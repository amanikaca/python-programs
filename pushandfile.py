import time

# Open a file in write mode
with open("output.txt", "w") as f:
    for i in range(5):
        # Print to file with flush=True to immediately write
        print(f"Line {i+1}", file=f, flush=True)
        print(f"Printed Line {i+1} to file and flushed buffer.")
        time.sleep(1)  # Pause 1 second to simulate delay

print("Done writing to output.txt")

#output

#C:\Users\Dell\Desktop\-\Python>py pushandfile.py
#Printed Line 1 to file and flushed buffer.
#Printed Line 2 to file and flushed buffer.
#Printed Line 3 to file and flushed buffer.
#Printed Line 4 to file and flushed buffer.
#Printed Line 5 to file and flushed buffer.
#Done writing to output.txt
