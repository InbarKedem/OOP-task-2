# building the child class for a with the child's name, age, energy level and focus time.
class Child:
    default_age = 8

    def __init__(self, name, age, energy_level, focus_time_hours):
        self.name = name
        self.age = age
        self.energy_level = energy_level
        self.focus_time_hours = focus_time_hours

    def getAge(self):
        # returns age if its between 6 and 12 else returns the default
        if self.age < 6 or self.age > 12:
            return self.default_age
        return self.age

    def getFocusTime(self):
        # gets focus time before break in hours
        return self.focus_time_hours

    def __str__(self):
        # returns a string that describes the child
        return f"{self.name}, Age: {self.getAge()}, Energy: {self.energy_level}, Focus: {self.focus_time_hours}h"

# building the interest group class that describes children's interest in the camp
# and includes a list of all the children
class InterestGroup:
    def __init__(self, name):
        self.name = name
        self.Children_list = []

    def addChild(self, child):
        # adds a child to the list
        self.Children_list.append(child)

    def removeChild(self, child):
        # removes a child from the list, only if they are in the list
        if child in self.Children_list:
            self.Children_list.remove(child)

    def groupAverageAge(self):
        # gets the group average age if there's anyone is the group otherwise 0
        if not self.Children_list:
            return 0
        return sum(child.getAge() for child in self.Children_list) / len(self.Children_list)

    def minFocusTime(self):
        # returns the minimum focus time among all children in the group. (If the group is empty, return -1)
        if not self.Children_list:
            return -1
        return min(child.getFocusTime() for child in self.Children_list)

    def __len__(self):
        # returns the length of the children list
        return len(self.Children_list)

    def __str__(self):
        # returns the required string and checks if it's empty.
        if not self.Children_list:
            return f"This group has no children."
        else:
            return f"Group {self.name}:\n" + "\n".join(str(child) for child in self.Children_list)

    def __add__(self, other):
        # the function for d that joins two groups
        new_name = f"{self.name}+{other.name}"  # joins their names
        # if one of the groups is AdvancedInterestGroup -> the result is also AdvancedInterestGroup
        if isinstance(self, AdvancedInterestGroup) or isinstance(other, AdvancedInterestGroup):
            # max required focus of the two (0 if one side is regular)
            req_focus = 0
            if isinstance(self, AdvancedInterestGroup):
                req_focus = max(req_focus, self.required_focus_time)
            if isinstance(other, AdvancedInterestGroup):
                req_focus = max(req_focus, other.required_focus_time)
            new_group = AdvancedInterestGroup(new_name, req_focus)
        else:
            new_group = InterestGroup(new_name)
        # makes sure there are no duplicates
        for child in self.Children_list + other.Children_list:
            if child not in new_group.Children_list:
                # Use InterestGroup.addChild to bypass the check in AdvancedInterestGroup
                # as the instruction requires including ALL children.
                InterestGroup.addChild(new_group, child)
        return new_group

    # this is the function for e that will add all the children from group 1 to group2
    # considering focus hours if needed
    def __iadd__(self, other):
        for child in other.Children_list:
            # avoid duplicates
            if child not in self.Children_list:
                # for AdvancedInterestGroup this will use the overridden addChild
                self.addChild(child)
        return self
    
# creating the advanced interest group that sets required hours
class AdvancedInterestGroup(InterestGroup):
    def __init__(self, name, required_focus_time):
        super().__init__(name)
        self.required_focus_time = required_focus_time

    def setRequiredFocus(self, time):
        self.required_focus_time = time

    def addChild(self, child):
        if child.getFocusTime() >= self.required_focus_time:
            InterestGroup.addChild(self, child)

    def __str__(self):
        children_str = "\n".join(str(child) for child in self.Children_list)
        return f"Advanced group {self.name} (required focus: {self.required_focus_time}h):\n{children_str}"

child1 = Child("Eden", 10, 90, 4)
child2 = Child("Ziv", 7, 80, 3)
child3 = Child("Dana", 5, 70, 2)
child4 = Child("Zohara", 12, 85, 5)
child5 = Child("Yosef", 11, 75, 6)

group1 = InterestGroup("Art")
group1.addChild(child1)
group1.addChild(child2)

adv_group1 = AdvancedInterestGroup("Robotics", required_focus_time=4)
adv_group1.addChild(child1)
adv_group1.addChild(child2)
adv_group1.addChild(child4)

adv_group2 = AdvancedInterestGroup("Music", required_focus_time=3)
adv_group2.addChild(child2)
adv_group2.addChild(child3)
adv_group2.addChild(child5)

print(group1)
print(adv_group1)
print(adv_group2)

merged_group = group1 + adv_group1
print("\nMerged Group (group1 + adv_group1):")
print(merged_group)

adv_group2 += adv_group1
print("\nAdvanced Group 2 after += adv_group1:")
print(adv_group2)