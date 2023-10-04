from random import choice

capital = "Topeka"

bird = "Wester MeadowLark"

flower  = "Sunflower"

song="Home on the range"

def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is kansas city",
        "A considerable protion of Kansas city is actually in Missouri",
        "Most Kansas are annoyed by Wizard of Oz references form people outside of Kansas."
    ]

    index = choice("0123")

    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()                  