# coding_skill.py   
import sys
import json

def main():
    
    sys.argv[0] = 'coding_skills.py'
    filename = sys.argv[1]
    #programing_list = ['C++', 'PHP', 'Python', 'C#', 'Haskell', 'Java', 'JavaScript', 'Ruby', 'CSS', 'C']
    with open(filename) as f:
        js = json.load(f)
        result = {}
        for person in js['people']:
            
            for n in person['skills']:  # n = skill !!!
                if n['name'] not in result:
                    result[n['name']] = (n['level'], person["first_name"], person["last_name"])
                else:
                    if n['level'] > result[n['name']][0]:
                        result[n['name']] = (n['level'], person["first_name"], person["last_name"])

        for lang_name, names in result.items():
            print(lang_name, '-', names[1], names[2])
            
            


if __name__ == '__main__':
    main()
