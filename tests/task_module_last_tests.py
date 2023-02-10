from ansiblelint.rules import RulesCollection
from ansiblelint.runner import Runner
from rules.task_module_last import TaskModuleLastRule

rule = TaskModuleLastRule()
collection = RulesCollection()
collection.register(rule)
test_playbooks_dir = f'tests/playbooks/{rule.id}'

def test_file_positive() -> None:
    """Positive test for task_module_last."""
    success = f'{test_playbooks_dir}/success.yml'
    good_runner = Runner(success, rules=collection)
    print(success)
    try:
        assert [] == good_runner.run()
    except Exception as e:
        print(e)
        assert False

def test_file_negative() -> None:
    """Negative test for task_module_last."""
    fail = f'{test_playbooks_dir}/fail.yml'
    bad_runner = Runner(fail, rules=collection)
    print(fail)
    try:
        errors = bad_runner.run()
        assert 2 == len(errors)
    except Exception as e:
        print(e)
        assert False