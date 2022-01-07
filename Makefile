PROJECT=tp-experimentateur
AUTHOR=FIL-ASD

.PHONY: clean doc archive author

clean:
	rm -f *~ */*~
	rm -rf __pycache__ src/__pycache__
	rm -rf $(DOC)
	rm -f $(PROJECT).zip
	rm -f conf.py-e
	rm -f */*.pyc
	rm -rf .DS_Store

doc: author
	mkdocs build

archive:
	rm -f $(PROJECT).zip
	zip -r $(PROJECT).zip . -x "sol/*" -x "site/*" -x "*~" -x "*.pyc" -x "*.DS_Store" -x "*__MACOSX/*" -x "*__pycache__/*"

author:
	sed -i -e 's/^site_name:.*/site_name: "Module $(PROJECT)"/g' mkdocs.yml
	sed -i -e 's/^copyright:.*/copyright: "2015-2022, $(AUTHOR), Univ. Lille"/g' mkdocs.yml
	sed -i -e 's/^site_author:.*/site_author: "$(AUTHOR)"/g' mkdocs.yml
