# validate that we can build
echo "Validate build requirments"
# pylint
if ! [ -x "$(command -v pylint)" ]; then
    echo 'pylint is not installed.'
    exit 1
fi

# yamllint
if ! [ -x "$(command -v yamllint)" ]; then
    echo 'yamllint is not installed.'
    exit 1
fi



# pylint all python files
for i in `find $(pwd) -name "*.py"`
do
  echo "pylint : "$i
  pylint -E $i
done

# yamllint all yaml file
for i in `find $(pwd) -name "*.yaml"`
do
  echo "yamllint : "$i
  yamllint $i
done

