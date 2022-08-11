# S&Q Animal Shelter
<!-- Short summary or background information -->
- Create a class called AnimalShelter which holds only dogs and cats.
  - The shelter operates using a first-in, first-out approach.
  - Implement the following methods:
    - enqueue
      - Arguments: animal
      - animal can be either a dog or a cat object.
    - dequeue
      - Arguments: pref
      - pref can be either "dog" or "cat"
      - Return: either a dog or a cat, based on preference.
        - If pref is not "dog" or "cat" then return null.
  - Stretch Goal
    - If a cat or dog isn’t preferred, return whichever animal has been waiting in the shelter the longest.

## Challenge
<!-- Description of the challenge -->
Bring in functionality for Queues and implement in context to pass tests. 

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
### Space
O(N) - Queueing as many animals as come into the shelter

### Time
O(N) - Depending on the function, max O(N) because animals are only enqueued or dequeued once

## API
<!-- Description of each method publicly available to your Stack and Queue-->