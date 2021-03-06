#-*- coding: utf-8 -*-
'''
Created on 2017. 04. 14
Updated on 2017. 04. 14
'''

from commons import Subjects
from commons import VersionUtil
import os
import shutil


class CopyResults(object):
	__name__ = 'CopyResults'

	def __init__(self, ):
		pass

	def run(self, _group, _project, _versions, _src, _dest):
		'''
		create result file
		'''


		techniques = ['BLIA']#'BugLocator', "BRTracer"]#, 'BLUiR', 'BLIA','AmaLgam', 'Locus']

		for tech in techniques:
			for version in _versions:
				vname = VersionUtil.get_versionName(version, _project)
				src_path = os.path.join(_src, '%s_%s_%s' % (tech, _project, vname), 'recommended')
				if os.path.exists(src_path) is False:
					print(('%s is not exists!!'%src_path))
					continue
				target_path = os.path.join(_dest, tech, _group, _project, '%s_%s' % (tech, vname))
				shutil.copytree(src_path, target_path)
				print(('%s is Done!!' % src_path))
		pass


###############################################################################################################
###############################################################################################################
###############################################################################################################
if __name__ == "__main__":
	import os
	WorkType = 'Full'
	S = Subjects()
	for group in S.groups:  # ['Commons', 'JBoss', 'Wildfly', 'Spring']
		for project in S.projects[group]:

			obj = CopyResults()
			obj.run(group, project,
					S.versions[project],
					S.getPath_result_folder(WorkType, group, project),
					os.path.join(S.root_result, 'organize_full'))
	pass

