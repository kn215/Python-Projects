def make_shirt(shirt_size= 'large', shirt_message= 'I love Python!'):
    """A function for describing a t-shirt"""
    print(f"\nYour size {shirt_size} shirt is read for pick up")
    print(f"It has the following message '{shirt_message.title()}'")

make_shirt()
make_shirt(shirt_size= 'medium') 
make_shirt('medium', 'fly eagles fly')
make_shirt(shirt_size= 'large', shirt_message= 'go birds')