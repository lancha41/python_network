import sys

sys.path.append("..")

from pyneng_common_functions import check_pytest

check_pytest(__loader__, __file__)


def test_task_stdout(capsys):
    """
    testing
    """
    import task_4_1

    out, err = capsys.readouterr()
    correct_stdout = (
        "ip nat inside source list ACL interface GigabitEthernet0/1 overload"
    )
    assert (
        out
    ), "please use print"
    assert (
        correct_stdout == out.strip()
    ), "icorrect"
