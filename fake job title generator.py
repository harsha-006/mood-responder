import random
adj_list=['Cybermetic','Virtual','Supreme','Legendary','Global','Nebulous','Cosmic','Revolutionary','Mindful','Parallel']
role_list=['Innovator','Hacker','Architect','Engineer','Strategist','Pioneer','Sage','Commander','Curator','MetaAnalyst']
suff_list=['Mastermind','Agent','Meme','Nomad','Unicorn','Hero','Maestro','Ranger','Captain','Navigator']
def fake_job(adj_list,role_list,suff_list,length):
    fake_title=[]
    for i in range(length):
        adj=random.choice(adj_list)
        role=random.choice(role_list)
        suff=random.choice(suff_list)
        title=(f"Fake Title has been created:'{adj}_{role}-{suff}'")
        fake_title.append(title)
    return fake_title
while True:
    length=int(input("Enter the count to generate the fake titles:"))
    titles=fake_job(adj_list,role_list,suff_list,length)
    for title in titles:
        print(title)
        
    extra=input(f"Still do u want more titles??? Say:(Yes/No)").strip().lower()
    if extra in ['no','n']:
        print("Thanks for using Fake_Job_Title_Generator")
        break