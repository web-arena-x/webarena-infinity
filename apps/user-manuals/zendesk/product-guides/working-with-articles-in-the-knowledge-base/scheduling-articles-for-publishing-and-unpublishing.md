# Scheduling articles for publishing and unpublishing

Source: https://support.zendesk.com/hc/en-us/articles/4408820403226-Scheduling-articles-for-publishing-and-unpublishing

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Enterprise |

Location:  Article editor > Save button menu > Schedule article

You can schedule articles to automatically publish or unpublish at a specific day and time in
your help center, and copy the schedule over to translated versions of the article (schedules
are stored individually per translation).

Anyone with publishing permissions can schedule an article for publishing or unpublishing.
Scheduled publishing and unpublishing is only available on Enterprise plans.

This article covers the following topics:

- [Setting scheduled publishing and unpublishing for an article](#topic_kch_gsx_s3b)
- [Setting scheduled unpublishing for a published article](#topic_dxt_rqp_jkb)
- [Editing scheduled publishing or unpublishing for an article](#topic_x4p_hsx_s3b)
- [Removing scheduled publishing or unpublishing of an article](#topic_rzz_gsx_s3b)

## Setting scheduled publishing and unpublishing for an article

You can set a specific time and day for an article to automatically be published and then
unpublished in your help center. You can apply the same schedule to translated versions of
the article.

You can also schedule articles for publishing and unpublishing in bulk. See [Updating knowledge base articles in bulk](https://support.zendesk.com/hc/en-us/articles/4408836336154).

**To schedule an individual article for both publishing and unpublishing**

1. Open an article in any workflow state in edit mode.
2. Make any necessary updates, then click **Save**.

   If the article is currently
   Published, you'll need to save the article in any other workflow state. If you want to
   set unpublishing for a published article, see [Setting scheduled unpublishing for a published article](#topic_dxt_rqp_jkb).
3. When you are ready to schedule your article, click the drop-down arrow on the Save
   button, then select **Schedule article**.

   ![hc_men_schedule_publishing](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-schedule-article-newui.jpg)
4. Select a date, time, and time zone for publishing the article.
   - **Date**: Select any future date from the calendar.
   - **Time**: Select a time from the drop-down options, available at one-hour
     intervals.
   - **Time zone**: Change the time zone if necessary. The default time zone is the
     user's time zone set in the user profile.

     Note: If your geography observes daylight
     savings time, consider this when setting the time for publication, because the
     scheduler will reflect and publish based on the time zone in effect at the point
     of publication (for example, PDT instead of PST).

   ![hc_schedule_article](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_schedule_article.png)
5. Click **Schedule to unpublish article** to additionally set a date, time, and time
   zone to unpublish the article.

   Note: The unpublish date and time must be after the
   publish date and time.

   You can come back and set an unpublish date while the
   article is approved for publishing, or alternatively set it after you've published the
   article. See [Setting scheduled unpublishing for a published article](#topic_dxt_rqp_jkb).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-article-schedule-header.png)
6. If you have translations of the article, click the **Apply schedule to all x
   translations of this article** checkbox to apply the schedule to all
   translations.

   Schedules are stored individually for each translation, but the
   checkbox copies the current schedule to all translations.

   Note: If you don't click
   the checkbox, your translated content is not included in the publishing schedule and
   you'll need to manually set the publish schedule for each translated
   version.
7. Click **Schedule**. If you have translations and have not applied the schedule to
   those versions of the article, you'll be prompted to flag the translations if they are
   outdated as a result of the update.
8. Toggle the radio button to flag any affected translations, and click
   **Close**.

   The schedule details are displayed in the article edit mode view and
   appear as "Scheduled" in article lists until the article is published. You can view a
   list of all scheduled articles in the Approved for Publishing article list. See [Viewing articles in various workflow states](https://support.zendesk.com/hc/en-us/articles/4408822216218).

   ![Scheduled for publishing icon](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-schedule-art-header.png)

   If anyone edits the article and tries to save before the scheduled
   publishing, they will be alerted about the schedule and given the option to save and
   remove the schedule or save and keep the schedule.

At the designated day and time, the article is published automatically. Anyone following
the article will receive email notification when the article is published, including the
person who scheduled the publishing, if they are following the article. Normally, when an
author publishes an article they do not receive notification.

If an unpublishing schedule has been set, the article is unpublished at the designated day
and time, and the article will revert to Work in progress status.

## Setting scheduled unpublishing for a published article

You can set a specific time and day for any published article to be unpublished in your
help center, for example, if you want to automatically unpublish an article after a certain
period of time.

You can also schedule articles for unpublishing in bulk. See [Updating knowledge base articles in bulk](https://support.zendesk.com/hc/en-us/articles/4408836336154).

**To schedule an individual published article for unpublishing**

1. Open an article that is in the Published workflow state.
2. Click the drop-down arrow on the Save button, then select **Schedule
   article**.

   ![hc_men_schedule_publishing](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-schedule-article-published-newui.jpg)
3. Select a date, time, and time zone for unpublishing the article.
   - **Date**: Select any future date from the calendar.
   - **Time**: Select a time from the drop-down options, available at one-hour
     intervals.
   - **Time zone**: Change the time zone if necessary. The default time zone is the
     user's time zone set in the user profile.

     Note: If your geography observes daylight
     savings time, consider this when setting the time for publication, because the
     scheduler will reflect and publish based on the time zone in effect at the point
     of publication (for example, PDT instead of PST).

   ![hc_schedule_article](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_schedule_article_unpublish.png)
4. Click **Schedule**.

   The article continues to appear as "Published" in article
   lists until it is unpublished.

   Users can edit or change the workflow of the
   article before the scheduled unpublishing, but unless they [edit](#topic_x4p_hsx_s3b) or [remove](#topic_rzz_gsx_s3b) the schedule itself, the
   article will be unpublished at the designated day and time.

At the designated day and time, the article will be unpublished automatically and the
article will revert to Work in progress status.

## Editing scheduled publishing or unpublishing for an article

You can edit the day, time, and time zone that an article is scheduled to be published or
unpublished.

**To edit the publishing or unpublishing schedule for an article**

1. Open any article that is scheduled for publishing or unpublishing in edit
   mode.

   Articles to be published appear in the Scheduled for Publishing article list.
   See [Viewing articles in various workflow states](https://support.zendesk.com/hc/en-us/articles/4408822216218).
2. Click the options menu on the schedule, then select **Edit schedule**.

   ![Scheduled publishing unpublishing menu](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Schedule-edit-schedulwe.png)
3. Edit the day, time, or time zone for publish and unpublish schedules.
4. Click **Schedule**.

## Removing scheduled publishing or unpublishing of an article

You can remove the scheduled publishing or unpublishing of an article.

**To remove the scheduled publishing or unpublishing of an article**

1. Open any article that is scheduled for publishing or unpublishing in edit
   mode.

   Articles to be published appear in the Scheduled for Publishing article list.
   See [Viewing articles in various workflow states](https://support.zendesk.com/hc/en-us/articles/4408822216218).
2. Click the options menu on the schedule, then select **Remove schedule**.

   ![Scheduled publishing unpublishing menu](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/schedule-remove-sachedule.png)
3. Click **Remove schedule** to confirm that you want to remove the scheduled
   publishing or unpublishing of this article.

   Note: If you have both publish and unpublish dates set for the article, you can't
   choose a schedule. Both schedules are removed.