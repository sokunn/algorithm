def gnome_sort(seq):
    i = 1
    while i < len(seq):
        if i == 0 or seq[i - 1] <= seq[i]:
            i += 1
        else:
            seq[i - 1], seq[i] = seq[i], seq[i - 1]
            i -= 1
    return seq


def test_gnome_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert (gnome_sort(seq) == sorted(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_gnome_sort()
