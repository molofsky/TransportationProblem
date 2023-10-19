class TransporationProblem(object):
  def __init__(self, N):
    # N = number of blocks
    self.N = N
  def startState(self):
    return 1
  def isEnd(self, state):
    return state == self.N
  def succAndCost(self, state):
    # return list of (action, newState, cost) triples
    return [('walk', state+1, 1) if state+1 <= self.N] or [('tram', state*2, 2) if state*2 <=self.N]
