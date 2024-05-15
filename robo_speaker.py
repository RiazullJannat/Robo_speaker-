import os
if __name__ == '__main__':
    print("Wellcome to robo_speaker 0.1")
    while True:
        inp = input("Enter what you want me to speak: ")
        if inp == 'q':
            os.system('say Good bye.')
            break
        os.system(f"say {inp}")

