# -*- coding: utf-8 -*-



s1 = '''
Born in New York City on October 11, 1884, Eleanor Roosevelt—the niece of Theodore Roosevelt—was
one of the most outspoken women in the White House. She married Franklin D. Roosevelt in 1905.
During her husband's presidency, Eleanor gave press conferences and wrote a newspaper column.
After his death, she served at the United Nations, focusing on human rights and women's issues.

Early Life

First lady, writer and humanitarian Eleanor Roosevelt was born Anna Eleanor Roosevelt on
October 11, 1884, in New York City. The niece of President Theodore Roosevelt, Eleanor was known
as a shy child, and experienced tremendous loss at a young age: Her mother died in 1892 and her
father died two years later, when she was just 10 years old. Eleanor was sent to school in England
when she was a teenager—an experience that helped draw her out of her shell.

In 1905, Eleanor married her distant cousin, Franklin D. Roosevelt, who would later become president
of the United States. Despite her busy home life, Eleanor became active in public service during
World War I, working for the American Red Cross.

U.S. First Lady

After her husband suffered a polio attack in 1921, Eleanor stepped forward to help Franklin with his
political career. When her husband became president in 1933, Eleanor dramatically changed the role
of the first lady. Not content to stay in the background and handle domestic matters, she showed the
world that the first lady was an important part of American politics. She gave press conferences and
spoke out for human rights, children's causes and women's issues, working on behalf of the League of
Women Voters. She even had her own newspaper column, "My Day." She also focused on helping the
country's poor, stood against racial discrimination and, during World War II, traveled abroad to
visit U.S. troops.

For her active role in public policy, Eleanor was heavily criticized by some. She was praised by
others, however, and today, she is regarded by as a leader of women's and civil rights, as well
as one of the first public officials to publicize important issues through the mass media.

Life After the White House

Following her husband's death, on April 12, 1945, Eleanor told interviewers that she didn't have
plans for continuing her public service: "The story is over," she reportedly stated. However,
the opposite would actually prove to be true. From 1945 to 1953, Eleanor served as a delegate
to the United Nations General Assembly. She also became chair of the UN's Human Rights Commission.
As a member of the Human Rights Commission, she helped to write the Universal Declaration of
Human Rights—an effort that she considered to be her greatest achievement.

Outside of her political work, Eleanor wrote several books about her life and experiences, including
This Is My Story (1937), This I Remember (1949), On My Own (1958) and Autobiography (1961).
She made a return to public service the same year her autobiography was published (1961), when
President John F. Kennedy made her a delegate to the United Nations. President Kennedy also
appointed Eleanor chair of the Commission on the Status of Women.

Death and Legacy

Eleanor died of cancer on November 7, 1962, at the age of 78. A revolutionary first lady,
Eleanor Roosevelt was one of the most outspoken women to live in the White House.
While she's had her share of critics, most agree that she was a great humanitarian
who dedicated much of her life to fighting for political and social change.

'''

'''
Questions:

1) (3 points) Use regular expression to find - How many times Eleanor is mentioned in the above passage.
2) (3 points) Use regular expression to find the number of times United Nations is mentioned in the above passage .
3) (2 points) Mention the books that Eleanor wrote. Read the passage and print the results.
4) (2 points) To how many presidents was Eleanor related to? Read the passage and print their names.
'''

import re


patterns = ['Eleanor','United Nations']
for p in patterns:
    print len(re.findall(p, s1))

books = ['This Is My Story (1937)', 'This I Remember (1949)', 'On My Own (1958)' , 'Autobiography (1961)']
for b in books:
    print b
    
print re.findall("This Is My Story (1937)",s1)
    
presidents =['Theodore Roosevelt','Franklin D. Roosevelt', 'John F. Kennedy']
for p in presidents:
    print p


