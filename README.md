# Restaurant Simulation
This **Restaurant Simulation** project models a restaurant environment where customers arrive, queue at billing counters, place burger orders, and wait for their food to be cooked. The simulation uses various data structures to manage customer queues, order processing, and burger cooking times.

## Table of Contents
- Overview
- Features
- Requirements
- Installation
- Usage

## Overview
This project simulates a restaurant with multiple billing counters and a griddle for cooking burgers. Customers arrive at the restaurant, queue for ordering burgers, and wait for their food to be prepared. The project uses different data structures to manage queues and priorities, providing a realistic model of how a restaurant might handle orders during busy periods.

## Features
- Customer Queuing: Simulates customer arrivals, queueing at billing counters, and tracking each customer’s order.
- Order Processing: Orders are processed based on counter availability and cooking capacity.
- Time Management: Tracks arrival and waiting times, advancing the simulation time in units to observe the status of counters and orders.
- State Management: Displays the current state of each customer and the griddle.
- Performance Metrics: Calculates and displays customer wait times and the average wait time for all customers.

## Requirements
- Python 3.x

The following data structures are utilized in the project:
- Sll_queue (from sll_queue.py)
- HeapPriorityQueue (from Priority_Queue.py)

## Installation
Clone the repository and navigate to the directory:
- `git clone https://github.com/shravanbishnoi/Restaurant-Simulation/`
- `cd Restaurant-Simulation/`
- Make sure all required files are in the same directory, as the main simulation code (Restaurant.py) depends on other modules like sll_queue.py and Priority_Queue.py.

## Usage
1. Run the simulation by executing the Restaurant.py file:
`python Restaurant.py`

2. The script simulates customer arrivals, advances time, and checks the states of counters, griddles, and customer wait times. Output displays each customer's state at various time intervals, patties on the griddle, wait times, and the average wait time.
  
3. Sample Simulation Steps (as included in Restaurant.py):
- Initialize the restaurant with a specified number of counters and griddle capacity.
- Simulate customer arrivals, checking queue and griddle states as time progresses.
- Print the wait times for each customer and the average wait time.
