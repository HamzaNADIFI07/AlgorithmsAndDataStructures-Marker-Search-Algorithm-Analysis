# -*- coding: utf-8 -*-

"""
Test module for experiences assignment

Note: Author
      [Dpt Informatique - FST - Univ. Lille](http://portail.fil.univ-lille1.fr)
      2018, january
"""

import sys
import experience
import marker
from functools import cmp_to_key

import sorting

def compare (m1,m2):
    '''
    Compares two markers

    Args:
      m1 (Marker): A marker 
      m2 (Marker): Another marker
    
    Returns:
      int: -1 if `m1 < m2`, 0 if `m1 = m2` or 1 when `m1 > m2`
    '''
    return m1.cmp(m2)

# STRATEGY 1
def negative_markers1(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.

    Args:
      markers (list of Marker): The list of markers 
      positive (list of Marker): The list of positive markers

    Returns:
      list of Marker: The list of negative markers
    """
    # Liste pour stocker les marqueurs négatifs
    negative = []
    for marker in markers:
        # Réinitialisation de trouve pour chaque marqueur
        trouve = False
        for pos_marker in positive:
            if compare(marker, pos_marker) == 0:
                trouve = True
                # On s'arrête dès qu'on trouve le marqueur à la liste des marqueurs positif
                break
        if not trouve:
            negative.append(marker)
    return negative


# STRATEGY 2
def negative_markers2(markers,positive):
    negative = []
    # Trier `positive` grâce au module sorting, qui vous est fourni (pensez à l'importer)
    positive_merged = sorting.merge_sort(positive, compare)  # Tri des positifs
    for marker in markers:
        debut = 0
        fin = len(positive_merged) - 1
        trouve = False
        while debut <= fin:
            milieu = (debut + fin) // 2
            element_milieu = positive_merged[milieu]
            if compare(element_milieu, marker) == 0:
                trouve = True
                break
            elif compare(element_milieu, marker) < 0:
                debut = milieu + 1
            else:
                fin = milieu - 1
        if not trouve:
            negative.append(marker)
    return negative



# STRATEGY 3
def negative_markers3(markers, positive):
    negative = []
    ensemble = markers + positive
    ensemble_merged = sorting.merge_sort(ensemble, compare)
    
    i = 0
    while i < len(ensemble_merged):
        if (i == 0 or compare(ensemble_merged[i], ensemble_merged[i-1]) != 0) and (i == len(ensemble_merged)-1 or compare(ensemble_merged[i], ensemble_merged[i+1]) != 0):
            negative.append(ensemble_merged[i])
        i += 1

    return negative

        
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: {} <p> <m>\n\n<p>: nombre de marqueurs positifs\n<m>: nombre de marqueurs".format(sys.argv[0]))
        sys.exit(1)
    p = int(sys.argv[1])
    m = int(sys.argv[2])

    assert (m > 0), "The number of markers must be greater than 0"
    assert (p <= m), "The number of positive markers must be less or equal to the number of markers"
    
    exp = experience.Experience(p,m)
    markers = exp.get_markers()
    positive = exp.get_positive_markers()

    print("Markers: {}".format(markers))
    print("Positive markers: {}".format(positive))
    
    # test stategy 1
    cpt = 0                     # D'après vous à quoi peut servir cette variable ? …
    print("Negative markers: {}".format(negative_markers1(markers,positive)))
    print("Nb. comparisons: {}".format(cpt))

    # test stategy 2
    cpt = 0
    print("Negative markers: {}".format(negative_markers2(markers,positive)))
    print("Nb. comparisons: {}".format(cpt))

    # test stategy 3
    cpt = 0
    print("Negative markers: {}".format(negative_markers3(markers,positive)))
    print("Nb. comparisons: {}".format(cpt))
