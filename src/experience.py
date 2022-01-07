# -*- coding: utf-8 -*-

"""
Module to manage experiences

An experience is made of a set of markers and a subset of those
markers that have been tested positive. 

Note: Author
      [Dpt Informatique - FST - Univ. Lille](http://portail.fil.univ-lille1.fr)
      2018, january

"""

import random
import copy
import marker

class Experience:

    def __init__(self,p,m):
        """
        Creates the results of an experience on `p` positive markers
        among `m` markers.

        Args:
          p (int): The number of positive markers (must be less or equal 
                   than the numbers of markers in `m`)
          m (int): The number of markers (must be greater than 0)
        """
        assert (p <= m)
        self.markers = marker.Marker.markers(m)
        l = list(self.markers)
        random.shuffle(l)
        self.experience = l[0:p]

    def get_markers (self):
        """
        Returns:
          Array of Marker: The markers that have been tested during the experience.

        Examples:
          >>> e = Experience(6,10)
          >>> m = e.get_markers()
          >>> len(m)
          10
          >>> sorted([ repr(i) for i in m])
          ['m0', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9']
        """
        return self.markers
    
    def get_positive_markers (self):
        """
        Returns:
          Array of Marker: The positive markers.

        Examples:
          >>> e = Experience(10,100)
          >>> p = e.get_positive_markers()
          >>> len(p)
          10
        """
        return self.experience
        
if __name__ == "__main__":
    import doctest
    results = doctest.testmod()
    exit(results[0])
