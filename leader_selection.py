import random


members = [
    ['John', 'Mary', 'Peter', 'Jane'],
    ['Anne', 'Mike', 'Lucy', 'Wesley'],
    ['Ben', 'Faith', 'Brian', 'Betty']
    ]


group1_leader = random.choice(members[0])
group2_leader = random.choice(members[1])
group3_leader = random.choice(members[2])


print(f'Group One leader is -> {group1_leader}')
print(f'Group Two leader is -> {group2_leader}')
print(f'Group Three leader is -> {group3_leader}')
